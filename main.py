"""
Criar janela para gerenciamento de estoque

"""

import os
import sys
import mysql.connector
from datetime import datetime
from tabulate import tabulate
from functools import partial
from dateutil.relativedelta import relativedelta
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QTableView, QTableWidgetItem, QMessageBox
from caixa import Ui_MainWindow
from delete_item import Ui_Form
from pagamento import Ui_Form as Ui_Form2
# from estoque import Ui_form as Ui_Form3

# Janela de deletar linha
class Delete_Window(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Delete_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Deletar Item')


# Janela de pagamento
class PayWindow(QtWidgets.QWidget, Ui_Form2):
    def __init__(self, parent=None):
        super(PayWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.setWindowTitle('Pagamento')
        self.imprimir.setVisible(False)


# class EstoqueWindow(QtWidgets.QWidget, Ui_Form3):
#     def __init__(self, parent=None):
#         super(EstoqueWindow, self).__init__(parent)
#         self.setupUi(self)
#         self.setWindowTitle('Estoque')


# Janela principal
class GUI_cont(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        
        self.precos = []
        
        self.linhas = []
        
        self.setWindowTitle('Caixa')
        self.showMaximized()
        
        # Botão de confirmar item a ser inserido na lista de produtos
        self.btn_confirmar.clicked.connect(self.confirma_produto)
        
        # Iniciando as janelas
        self.delete_window = Delete_Window()
        self.payment_window = PayWindow()
        
        # Chama a função finaliza_compra quando o botão de finalizar compra for clicado 
        self.btn_finalizar_2.clicked.connect(self.finaliza_compra)
        self.payment_window.imprimir.clicked.connect(self.imprimir)
        # self.actionAdicionar_produto_ao_estoqeu.triggered(self.cadastra_action_triggered)
    
    
    # Função que é chamada para imprimir a nota da compra
    def imprimir(self):
        # pega o número de linhas que tem na tabela de produtos
        linhas_tabela = self.tabela_produtos.rowCount() - 1
        itens = []
        for n in range(linhas_tabela):
            itens.append([self.tabela_produtos.item(n, 0).text(), self.tabela_produtos.item(n, 1).text(), self.tabela_produtos.item(n, 2).text(), self.tabela_produtos.item(n, 3).text(), self.tabela_produtos.item(n, 4).text()])        
        
        try:
            # Cria um arquivo de texto com a data, valor total, produtos comprados e o método de pagamento 
            with open('caixa.txt', 'w') as f:
                data = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                
                f.write(f'Método de pagamento: {self.payment_window.metodo_pagamento.currentText()}\n\n')
                
                f.write(tabulate(itens, headers=['Código', 'Produto', 'Quantidade', 'Valor Unitário', 'Valor Total' ]))
                f.write('\n')
                
                f.write(f'\nTotal: R${sum(self.precos)}')
                f.write(f'\n\nData: {str(data)}')
                
                f.close()
                
            os.startfile('caixa.txt', 'print')
  
        except Exception as e:
            print(e)
    
        # Exclui todas as linhas de produtos da tabela de produtos
        for i in range(linhas_tabela):
            self.tabela_produtos.removeRow(0)
            
        # Exclui todos os itens da lista de preços
        self.precos = []
        # Retorna o valor de total para 0.00
        self.total_label.setText('Total: R$0.00')
        # Fecha a janela de pagamento
        self.payment_window.close()


    # Função para exibir msg de erro    
    def error_popup(self, msg):
        button = QMessageBox.critical(
            self,
            'Erro',
            msg,
            buttons = QMessageBox.StandardButton.Ok
        )
    
    
    # Função para conectar com a base de dados
    def connection(self):
        conn = mysql.connector.connect(
            host='localhost', 
            user='root', 
            password='Minuano95.', 
            database='produtos')
        cursor = conn.cursor()
        return conn, cursor
    
    
    def cadastra_action_triggered(self):
        # self.estoque_window.show()
        pass
    
    
    def cadastra_produto(self, nome, categoria, marca, preco, estoque):
        conn, cursor = self.connection()
        cursor.execute('INSERT INTO produto (nome, categoria, marca, preco, estoque) VALUES (%s, %s, %s, %s, %s)', (nome, categoria, marca, preco, estoque,))
        conn.commit()
        conn.close()
    
    
    def atualiza_produto(self, codigo, nome=None, categoria=None, marca=None, preco=None, estoque=None):
        conn, cursor = self.connection()
     
        produto = cursor.execute('SELECT * FROM produto WHERE codigo = %s', (codigo,))
        produto = cursor.fetchone()
        
        # Checa se o produto existe
        if produto:
            # checa se é o nome que vai ser alterado
            if nome is not None:
                cursor.execute('UPDATE produto SET nome = %s WHERE codigo = %s', (nome, codigo,))
            # checa se é a categoria que vai ser alterada
            if categoria is not None:
                cursor.execute('UPDATE produto SET categoria = %s WHERE codigo = %s', (categoria, codigo,))
            # checa se é a marca que vai ser alterada
            if marca is not None:
                cursor.execute('UPDATE produto SET marca = %s WHERE codigo = %s', (marca, codigo,))
            # checa se é o preço que vai ser alterado
            if preco is not None:
                try:
                    float(preco)
                    cursor.execute('UPDATE produto SET preco = %s WHERE codigo = %s', (preco, codigo,))
                except ValueError:
                    return False
            # checa se é o estoque que vai ser alterado
            if estoque is not None:
                try:
                    float(estoque)
                    cursor.execute('UPDATE produto SET estoque = %s WHERE codigo = %s', (estoque, codigo,))
                except ValueError:
                    return False
        else:
            return False

        conn.commit()
        conn.close()
    
    
    def deleta_produto(self, codigo):
        cursor, connection = self.connection()
        cursor.execute('DELETE FROM produto WHERE codigo = %s', (codigo,))
        connection.commit()
        connection.close()
    
   
    def altera_estoque(self, codigo, qnt):
        conn, cursor = self.connection()
        estoque = cursor.execute(f"SELECT estoque FROM produto WHERE codigo = %s", (estoque))
        if qnt > estoque:
            return False
        else:
            cursor.execute("UPDATE produtos SET estoque = %s WHERE codigo = %s", (estoque - qnt, codigo))
        conn.commit()
        conn.close()
    
    
    # Função que é chamada para excluir produto da tabela de produtos
    def deleta_produto_lista(self):
        
        # Pega o número da linha que vai ser excluida
        linha = self.delete_window.lineEdit.text()
        
        conn, cursor = self.connection()
        
        try:
            # faz o tratamento do dado
            int(linha)
            
            # pega a quantidade de linhas que tem na tabela de produtos
            linhas_lista_produtos = self.tabela_produtos.rowCount() - 1
            
            # se a linha não existir
            if int(linha) > linhas_lista_produtos or int(linha) == 0:
                self.error_popup('Linha não encontrada.')
            
            else:
                # exclui o preco da linha da tabela de preços
                self.precos.pop(int(linha) - 1)
                # atualiza o valor total
                self.total_label.setText(f'Total: R${str(sum(self.precos))}')
                # exclui a linha da tabela de produtos
                self.tabela_produtos.removeRow(int(linha) - 1)
                
                # atualiza o estoque do produto no banco de dados
                qnt = self.linhas[int(linha)-1][2]
                codigo = self.linhas[int(linha)-1][0]
                cursor.execute('SELECT estoque FROM produto WHERE codigo = %s', (codigo,))
                qnt_estoque = cursor.fetchone()[0]
                cursor.execute('UPDATE produto SET estoque = %s WHERE codigo = %s', (float(qnt) + float(qnt_estoque),codigo,))                
                
                self.delete_window.label_2.setText('')
                self.delete_window.lineEdit.setText('')
                self.delete_window.close()
        
        except ValueError:
            self.error_popup('A linha precisa ser um número inteiro.')
        
        finally:
            conn.commit()
            conn.close()
    
    
    # Função para abrir a janela de deletar produto da lista
    def keyPressEvent(self, event):
        
        if event.key() == QtCore.Qt.Key.Key_F10:
            self.delete_window.show()
            
            try:
                self.delete_window.error_msg.clicked.connect(self.deleta_produto_lista)
            
            except Exception as e:
                print(e, 'keypressevent')
    
                
    # Função que trata o dado e valida se o código existe
    def valida_codigo(self, codigo,):
        
        conn, cursor = self.connection()
        
        try:
            int(codigo)
            cursor.execute('SELECT * FROM produto WHERE codigo = %s', (codigo,))
            produto = cursor.fetchone()
        
            if produto:
                return produto
        
            else:
                self.error_popup('Código inválido.')
        
        except ValueError:
            self.error_popup('O código precisa ser um número.')
        
        finally:
            conn.close()
    
    
    # Função que trata o dado e valida se a quantidade solicitada está disponivel
    def valida_qnt(self, codigo, qnt):
        conn, cursor = self.connection()
        cursor.execute('SELECT estoque FROM produto WHERE codigo = %s', (codigo,))
        qnt_estoque = cursor.fetchone()[0]

        try:
            float(qnt)

            if float(qnt) > qnt_estoque:
                print('codigo', codigo)
                print('estoque', qnt_estoque)
                self.error_popup('Quantidade indisponível.')

            else:
                cursor.execute("UPDATE produto SET estoque = %s WHERE codigo = %s", (float(qnt_estoque - float(qnt)), codigo,))
                return qnt

        except ValueError:
            print('erro na quantidade')
            self.error_popup('A quantidade precisa ser um número.')

        finally:
            conn.commit()
            conn.close()
    

    # Função é chamada para adicionar um produto na tabela de produtos
    def confirma_produto(self):
        
        try:
            codigo_produto = self.codigo_input.text()
            produto = self.valida_codigo(codigo_produto,)
            qnt_produto = self.qnt_input.text()
            qnt = self.valida_qnt(codigo_produto, qnt_produto)
        
            if produto and qnt:
                # Adicionando o produto na tabela de produtos
                rowPosition = self.tabela_produtos.rowCount()
                self.tabela_produtos.insertRow(rowPosition)
                self.tabela_produtos.setItem(rowPosition-1, 0, QtWidgets.QTableWidgetItem(str(produto[0])))
                self.tabela_produtos.setItem(rowPosition-1, 1, QtWidgets.QTableWidgetItem(produto[1]))
                self.tabela_produtos.setItem(rowPosition-1, 2, QtWidgets.QTableWidgetItem(str(qnt)))
                preco = round(float(qnt)*produto[3], 2)
                self.precos.append(preco)
                self.tabela_produtos.setItem(rowPosition-1, 3, QtWidgets.QTableWidgetItem(str(float(produto[3]))))
                self.tabela_produtos.setItem(rowPosition-1, 4, QtWidgets.QTableWidgetItem(str(float(preco))))
                
                # Trocando o background das celulas
                self.tabela_produtos.item(rowPosition-1, 0).setBackground(QtGui.QColor(243,244, 245))
                self.tabela_produtos.item(rowPosition-1, 1).setBackground(QtGui.QColor(243,244, 245))
                self.tabela_produtos.item(rowPosition-1, 2).setBackground(QtGui.QColor(243,244, 245))
                self.tabela_produtos.item(rowPosition-1, 3).setBackground(QtGui.QColor(243,244, 245))
                self.tabela_produtos.item(rowPosition-1, 4).setBackground(QtGui.QColor(243,244, 245))
                
                # Alinhando eles no centro
                self.tabela_produtos.item(rowPosition-1, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.tabela_produtos.item(rowPosition-1, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.tabela_produtos.item(rowPosition-1, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.tabela_produtos.item(rowPosition-1, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.tabela_produtos.item(rowPosition-1, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                
                # Deixando os campos vazios para o usuário digitar o próximo produto
                self.total_label.setText(f'Total: R${str(sum(self.precos))}')
                self.codigo_input.setText('')
                self.qnt_input.setText('')
                
                self.linhas.append([produto[0], produto[1], qnt, preco])

        except Exception as e:
            print(e, 'confirma compra')


    # Função para finalizar a compra
    def finaliza_compra(self):
        
        self.payment_window.total_label.setText('')
        self.payment_window.recebido_input.setText('')
        self.payment_window.desconto_input.setText('')
        self.payment_window.total_valor_label_2.setText('R$0.00')
        self.payment_window.show()
        
        total = sum(self.precos)
        self.payment_window.total_label.setText(f'R${str(total)}')
        
        def troco():
            pagamento = self.payment_window.recebido_input.text()
            try:
                float(pagamento)
                if float(pagamento) < total:
                    self.error_popup('O valor recebido é menor que o valor da compra')
                else:
                    troco = round(float(pagamento) - total, 2)
                    self.payment_window.total_valor_label_2.setText(f'R${str(troco)}')
                    
                    conn, cursor = self.connection()
                    metodo = self.payment_window.metodo_pagamento.currentText()
                    cursor.execute('INSERT INTO vendas (data, valor, metodo) VALUES (%s, %s, %s)', (datetime.now(), float(total), metodo,))
                    conn.commit()
                    self.payment_window.confirmar_btn.setVisible(False)
                    self.payment_window.imprimir.setVisible(True)

            except ValueError:
                self.error_popup('O valor recebido precisa ser um número.')

            except Exception as e:
                print(e)
                
        self.payment_window.confirmar_btn.clicked.connect(troco)
        
    
app = QApplication(sys.argv)
window = GUI_cont()
window.show()
app.exec()