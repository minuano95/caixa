"""
Popup de campos vazios aparecendo na janela de cadastrar produtos
Trocar , por . na janela de pagamento da janela de vendas 
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
from mainwindow import Ui_MainWindow as MainWindow
from adicionar_item import Ui_Form as Ui_Form3
from estoque import Ui_Form as Ui_Form4
from deletar_produto import Ui_Form as Ui_Form5
from editar_produto import Ui_Form as Ui_Form6
from password import PASSWORD


# Janela para deletar linha
class Delete_Window(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Delete_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Deletar Item')
        self.setTabOrder(self.lineEdit, self.error_msg)


# Janela de pagamento
class PayWindow(QtWidgets.QWidget, Ui_Form2):
    def __init__(self, parent=None):
        super(PayWindow, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle('Pagamento')
        self.imprimir.setVisible(False)


# Janela para cadastrar item no estoque
class AdicionarItem(QtWidgets.QWidget, Ui_Form3):
    def __init__(self, parent=None):
        super(AdicionarItem, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Cadastrar Item')
        self.pushButton.clicked.connect(self.salva_produto)

    def error_popup(self, msg):
        button = QMessageBox.critical(
            self,
            'Erro',
            msg,
            buttons=QMessageBox.StandardButton.Ok
        )

    def connection(self):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=PASSWORD,
            database='produtos')
        cursor = conn.cursor()
        return conn, cursor

    def valida_codigo(self):
        codigo = self.lineEdit_5.text()
        try:
            int(codigo)
            conn, cursor = self.connection()
            cursor.execute(
                'SELECT * FROM produto WHERE codigo_barras = %s', (codigo,))
            codigo_existente = cursor.fetchall()
            if len(codigo_existente) > 0:
                if int(codigo) == int(codigo_existente[0]):
                    print(codigo, 'erro código')
                    self.error_popup('Código já existente.')
                    validou = False
                    return 0, validou
            else:
                validou = True
                return int(codigo), validou

        except ValueError:
            self.error_popup('Código inválido.')

    def salva_produto(self):
        validou = True

        try:

            codigo, validou = self.valida_codigo()
            produto = self.lineEdit.text()
            marca = self.lineEdit_2.text()
            categoria = self.lineEdit_4.text()

            if len(produto) < 1 or len(categoria) < 1:
                self.error_popup('Preencha todos os campos.')
                validou = False

            preco = self.lineEdit_6.text().replace(',', '.')
            qnt = self.lineEdit_3.text().replace(',', '.')

            try:
                float(preco)
            except ValueError:
                self.error_popup('Preço inválido.')
                validou = False

            try:
                float(qnt)
            except ValueError:
                self.error_popup('Quantidade inválida.')
                validou = False

            if validou:
                conn, cursor = self.connection()
                cursor.execute('INSERT INTO produto (codigo_barras, produto, categoria, preco, estoque, marca) VALUES (%s, %s, %s, %s, %s, %s)', (
                    codigo, produto, categoria, preco, qnt, marca,))
                conn.commit()
                conn.close()

                self.lineEdit.setText('')
                self.lineEdit_2.setText('')
                self.lineEdit_3.setText('')
                self.lineEdit_4.setText('')
                self.lineEdit_5.setText('')
                self.lineEdit_6.setText('')

                button = QMessageBox.information(
                    self,
                    'Cadastro',
                    'Produto cadastrado com sucesso!',
                    buttons=QMessageBox.StandardButton.Ok
                )
        except TypeError:
            pass


# Janela para mostar o estoque
class EstoqueWindow(QtWidgets.QWidget, Ui_Form4):
    def __init__(self, parent=None):
        super(EstoqueWindow, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle('Estoque')
        self.setMinimumSize(1366, 720)

        for n in range(self.tabela_produtos.rowCount()):
            self.tabela_produtos.removeRow(0)

        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=PASSWORD,
            database='produtos')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM produto')
        self.produtos = cursor.fetchall()

        self.tabela_produtos.setColumnWidth(0, 150)
        self.tabela_produtos.setColumnWidth(1, 691)
        self.show_produtos()

        self.pushButton.clicked.connect(self.pesquisa_produto)

    def pesquisa_produto(self):

        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=PASSWORD,
            database='produtos')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM produto')
        self.produtos = cursor.fetchall()

        if self.tabela_produtos.rowCount() > 0:
            for i in range(self.tabela_produtos.rowCount()):
                self.tabela_produtos.removeRow(0)

        item_encontrado = False
        metodo = self.comboBox.currentText()
        termo = self.lineEdit.text()

        rowPosition = self.tabela_produtos.rowCount()

        if termo == '':
            self.show_produtos()

        else:
            for produto in self.produtos:

                if metodo == 'Código':
                    try:
                        if int(termo) == int(produto[0]):
                            item_encontrado = True
                            self.tabela_produtos.insertRow(rowPosition)
                            self.tabela_produtos.setItem(
                                rowPosition, 0, QtWidgets.QTableWidgetItem(str(produto[0])))
                            self.tabela_produtos.setItem(
                                rowPosition, 1, QtWidgets.QTableWidgetItem(str(produto[1])))
                            self.tabela_produtos.setItem(
                                rowPosition, 2, QtWidgets.QTableWidgetItem(str(produto[2])))
                            self.tabela_produtos.setItem(
                                rowPosition, 3, QtWidgets.QTableWidgetItem(str(produto[3])))
                            self.tabela_produtos.setItem(
                                rowPosition, 4, QtWidgets.QTableWidgetItem(str(produto[4])))
                            self.tabela_produtos.setItem(
                                rowPosition, 5, QtWidgets.QTableWidgetItem(str(produto[5])))
                            break
                    except ValueError:
                        break
                        button = QMessageBox.critical(
                            self,
                            'Erro',
                            'O código precisa ser um número.',
                            buttons=QMessageBox.StandardButton.Ok
                        )

                try:
                    if metodo == 'Nome':
                        if termo in produto[1]:
                            item_encontrado = True
                            self.tabela_produtos.insertRow(rowPosition)
                            self.tabela_produtos.setItem(
                                rowPosition, 0, QtWidgets.QTableWidgetItem(str(produto[0])))
                            self.tabela_produtos.setItem(
                                rowPosition, 1, QtWidgets.QTableWidgetItem(str(produto[1])))
                            self.tabela_produtos.setItem(
                                rowPosition, 2, QtWidgets.QTableWidgetItem(str(produto[2])))
                            self.tabela_produtos.setItem(
                                rowPosition, 3, QtWidgets.QTableWidgetItem(str(produto[3])))
                            self.tabela_produtos.setItem(
                                rowPosition, 4, QtWidgets.QTableWidgetItem(str(produto[4])))
                            self.tabela_produtos.setItem(
                                rowPosition, 5, QtWidgets.QTableWidgetItem(str(produto[5])))

                except Exception as e:
                    print(e)

            print(item_encontrado)
            if item_encontrado == False:
                print('ta no else')
                for i in range(rowPosition):
                    self.tabela_produtos.removeRow(0)
                button = QMessageBox.critical(
                    self,
                    'Erro',
                    'Código ou nome não encontrado.',
                    buttons=QMessageBox.StandardButton.Ok
                )
                try:
                    self.show_produtos()
                except Exception as e:
                    print(e)

            item_encontrado = False

    def show_produtos(self):

        rowPosition = self.tabela_produtos.rowCount()
        for produto in self.produtos:
            self.tabela_produtos.insertRow(rowPosition)
            self.tabela_produtos.setItem(
                rowPosition, 0, QtWidgets.QTableWidgetItem(str(produto[0])))
            self.tabela_produtos.setItem(
                rowPosition, 1, QtWidgets.QTableWidgetItem(str(produto[1])))
            self.tabela_produtos.setItem(
                rowPosition, 2, QtWidgets.QTableWidgetItem(str(produto[2])))
            self.tabela_produtos.setItem(
                rowPosition, 3, QtWidgets.QTableWidgetItem(str(produto[3])))
            self.tabela_produtos.setItem(
                rowPosition, 4, QtWidgets.QTableWidgetItem(str(produto[4])))
            self.tabela_produtos.setItem(
                rowPosition, 5, QtWidgets.QTableWidgetItem(str(produto[5])))

    def keyPressEvent(self, event):

        if event.key() == QtCore.Qt.Key.Key_Enter:
            self.pesquisa_produto()

        if event.key() == QtCore.Qt.Key.Key_Return:
            self.pesquisa_produto()


# Janela para excluir produto
class DeletarProduto(QtWidgets.QWidget, Ui_Form5):
    def __init__(self, parent=None):
        super(DeletarProduto, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Deletar Produto')
        self.setFixedSize(self.size())
        self.pushButton.clicked.connect(self.pesquisa_item)
        self.pushButton_2.clicked.connect(self.excluir)

    def keyPressEvent(self, event):

        if event.key() == QtCore.Qt.Key.Key_Enter and self.pushButton.hasFocus():
            self.pesquisa_item()

        if event.key() == QtCore.Qt.Key.Key_Return and self.pushButton.hasFocus():
            self.pesquisa_item()

        if event.key() == QtCore.Qt.Key.Key_Enter and self.pushButton_2.hasFocus():
            self.excluir()

        if event.key() == QtCore.Qt.Key.Key_Return and self.pushButton_2.hasFocus():
            self.excluir()

    def excluir(self):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=PASSWORD,
            database='produtos')
        cursor = conn.cursor()
        if len(self.lineEdit.text()) < 1:
            button = QMessageBox.critical(self,
                                          'Erro',
                                          'Código não encontrado.',
                                          buttons=QMessageBox.StandardButton.Ok
                                          )

        else:
            cursor.execute(
                'DELETE FROM produto WHERE codigo_barras = %s', (self.lineEdit.text(),))
            conn.commit()
            button = QMessageBox.information(self,
                                             'Sucesso',
                                             'Item deletado com sucesso!',
                                             buttons=QMessageBox.StandardButton.Ok
                                             )
            self.label_2.setText('')
            self.label_6.setText('')
            self.label_7.setText('')

    def pesquisa_item(self):
        print(self.pushButton.hasFocus())
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password=PASSWORD,
                database='produtos')
            cursor = conn.cursor()
            cursor.execute(
                'SELECT * FROM produto WHERE codigo_barras = %s', (self.lineEdit.text(),))
            produto = cursor.fetchall()
            if len(produto) < 1:
                button = QMessageBox.critical(self,
                                              'Erro',
                                              'Código não encontrado.',
                                              buttons=QMessageBox.StandardButton.Ok
                                              )
            else:
                print(produto)
                self.label_2.setText(str(produto[0][0]))
                self.label_6.setText(str(produto[0][1]))
                self.label_7.setText(str(produto[0][5]))

        except Exception as e:
            print(e)


# Janela para editar o produto no estoque
class EditarProdutoWindow(QtWidgets.QWidget, Ui_Form6):
    def __init__(self, parent=None):
        super(EditarProdutoWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Editar Produto')
        self.setFixedSize(self.size())
        self.antigo_codigo = ''
        self.pesquisou = False

        self.pushButton.clicked.connect(self.pesquisa)
        self.pushButton_2.clicked.connect(self.edita)

    def pesquisa(self):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=PASSWORD,
            database='produtos')
        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM produto WHERE codigo_barras = %s', (self.lineEdit.text(),))
        produto = cursor.fetchall()
        if len(produto) < 1:
            button = QMessageBox.critical(self,
                                          'Erro',
                                          'Código não encontrado.',
                                          buttons=QMessageBox.StandardButton.Ok
                                          )
        else:
            self.antigo_codigo = produto[0][0]
            self.lineEdit_2.setText(str(produto[0][0]))
            self.lineEdit_3.setText(str(produto[0][1]))
            self.lineEdit_4.setText(str(produto[0][2]))
            self.lineEdit_5.setText(str(produto[0][3]))
            self.lineEdit_6.setText(str(produto[0][4]))
            self.lineEdit_7.setText(str(produto[0][5]))

            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            self.lineEdit_4.setEnabled(True)
            self.lineEdit_5.setEnabled(True)
            self.lineEdit_6.setEnabled(True)
            self.lineEdit_7.setEnabled(True)
            
            self.pesquisou = True
            
    def connection(self):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=PASSWORD,
            database='produtos')
        cursor = conn.cursor()
        return conn, cursor

    def error_popup(self, msg):
        button = QMessageBox.critical(
            self,
            'Erro',
            msg,
            buttons=QMessageBox.StandardButton.Ok
        )

    def valida_codigo(self):
        codigo = self.lineEdit_2.text()
        try:
            if len(codigo) > 0:
                codigo = int(codigo)
                return codigo, True
            else:
                self.error_popup('Código inválido.')
                return 0, False
            
        except ValueError:
            return False
            self.error_popup('Código inválido.')

    def valida_preco(self, codigo, preco):
        try:
            preco = float(preco.replace(',', '.'))

            conn, cursor = self.connection()
            cursor.execute("UPDATE produto SET preco = %s WHERE codigo_barras = %s", (preco, codigo,))
            conn.commit()
            return preco, True

        except ValueError:
            self.error_popup('O preço precisa ser um número.')
            return 0, False

    def valida_qnt(self, codigo, qnt):
        try:
            qnt = float(qnt.replace(',', '.'))

            conn, cursor = self.connection()
            cursor.execute("UPDATE produto SET estoque = %s WHERE codigo_barras = %s", (qnt, codigo,))
            conn.commit()
            return qnt, True

        except ValueError:
            self.error_popup('A quantidade precisa ser um número.')
            return 0, False
            
    def edita(self):
        
        if self.pesquisou:
            validou = True
            
            codigo, validou = self.valida_codigo()
            produto = self.lineEdit_3.text()
            categoria = self.lineEdit_4.text()
            preco, validou = self.valida_preco(codigo, self.lineEdit_5.text())
            try:
                qnt, validou = self.valida_qnt(codigo, self.lineEdit_6.text())
            except Exception as e:
                print(e)
            marca = self.lineEdit_7.text()

            if len(produto) < 1 or len(categoria) < 1:
                self.error_popup('Preencha todos os campos.')
                validou = False

            if validou:
                conn, cursor = self.connection()
                cursor.execute("UPDATE produto SET codigo_barras = %s, produto = %s, categoria = %s, preco = %s, estoque = %s, marca = %s WHERE codigo_barras = %s", (codigo, produto, categoria, preco, qnt, marca, codigo,))
                conn.commit()
                button = QMessageBox.information(self, 'Alterado', 'Produto alterado com sucesso!')
                self.lineEdit_2.setText('')
                self.lineEdit_3.setText('')
                self.lineEdit_4.setText('')
                self.lineEdit_5.setText('')
                self.lineEdit_6.setText('')
                self.lineEdit_7.setText('')



# Janela principal
class GUI_cont(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)

        self.precos = []
        self.itens = []
        self.linhas = []

        self.troco = 0
        self.total = 0.00

        self.setWindowTitle('Caixa')
        self.showMaximized()
        self.label_logo.setStyleSheet(
            'background-color: grey; color: black; font-size: 30px; font-weight: bold;')
        self.label_logo.setText('SUA LOGO AQUI')
        self.label_logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Botão de confirmar item a ser inserido na lista de produtos
        self.btn_confirmar.clicked.connect(self.confirma_produto)
        # self.btn_confirmar.releaseKeyboard()

        # Iniciando as janelas
        self.delete_window = Delete_Window()
        self.payment_window = PayWindow()

        self.tabela_produtos.setEnabled(False)
        self.tabela_produtos.setColumnWidth(0, 80)
        self.tabela_produtos.setColumnWidth(1, 223)
        self.tabela_produtos.setColumnWidth(2, 110)
        self.tabela_produtos.setColumnWidth(3, 105)
        self.tabela_produtos.setColumnWidth(4, 95)

        self.setTabOrder(self.codigo_input, self.qnt_input)
        self.setTabOrder(self.qnt_input, self.btn_confirmar)
        self.setTabOrder(self.btn_confirmar, self.btn_finalizar_2)
        self.setTabOrder(self.btn_finalizar_2, self.tabela_produtos)
        self.setTabOrder(self.tabela_produtos, self.codigo_input)

        # Chama a função finaliza_compra quando o botão de finalizar compra for clicado
        # self.btn_finalizar_2.clicked.connect(self.finaliza_compra)

        try:
            self.btn_finalizar_2.pressed.connect(self.finaliza_compra)
        except Exception as e:
            print(e)

        self.payment_window.imprimir.clicked.connect(self.imprimir)
        # self.payment_window.imprimir.pressed.connect(self.imprimir)
        # self.actionAdicionar_produto_ao_estoqeu.triggered(self.cadastra_action_triggered)

    # Função que é chamada para imprimir a nota da compra

    def imprimir(self):
        # pega o número de linhas que tem na tabela de produtos
        linhas_tabela = self.tabela_produtos.rowCount() - 1

        # Cria um arquivo de texto com a data, valor total, produtos comprados e o método de pagamento
        with open('caixa.txt', 'w', encoding="utf-8") as f:
            data = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

            f.write(
                f'Método de pagamento: {self.payment_window.metodo_pagamento.currentText()}\n\n')

            f.write(tabulate(self.itens, headers=[
                    'Código', 'Produto', 'Quantidade', 'Valor Unitário', 'Valor Total']))
            f.write('\n')
            # 400 x 84
            # 797 x 84
            f.write(f'\nTotal: R${self.total}')
            f.write(
                f'\nRecebido: R${self.payment_window.recebido_input.text()}')
            f.write(f'\nTroco: R${self.troco}')

            f.write(f'\n\nData: {str(data)}')

            f.close()

        os.startfile('caixa.txt', 'print')

        self.total = 0.00
        # Exclui todos os itens da lista de itens
        self.itens = []
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
            buttons=QMessageBox.StandardButton.Ok
        )

    # Função para conectar com a base de dados

    def connection(self):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=PASSWORD,
            database='produtos')
        cursor = conn.cursor()
        return conn, cursor

    def atualiza_produto(self, codigo, nome=None, categoria=None, marca=None, preco=None, estoque=None):
        conn, cursor = self.connection()

        produto = cursor.execute(
            'SELECT * FROM produto WHERE codigo_barras = %s', (codigo,))
        produto = cursor.fetchone()

        # Checa se o produto existe
        if produto:
            # checa se é o nome que vai ser alterado
            if nome is not None:
                cursor.execute(
                    'UPDATE produto SET nome = %s WHERE codigo_barras = %s', (nome, codigo,))
            # checa se é a categoria que vai ser alterada
            if categoria is not None:
                cursor.execute(
                    'UPDATE produto SET categoria = %s WHERE codigo_barras = %s', (categoria, codigo,))
            # checa se é a marca que vai ser alterada
            if marca is not None:
                cursor.execute(
                    'UPDATE produto SET marca = %s WHERE codigo_barras = %s', (marca, codigo,))
            # checa se é o preço que vai ser alterado
            if preco is not None:
                try:
                    float(preco)
                    cursor.execute(
                        'UPDATE produto SET preco = %s WHERE codigo_barras = %s', (preco, codigo,))
                except ValueError:
                    return False
            # checa se é o estoque que vai ser alterado
            if estoque is not None:
                try:
                    float(estoque)
                    cursor.execute(
                        'UPDATE produto SET estoque = %s WHERE codigo = %s', (estoque, codigo,))
                except ValueError:
                    return False
        else:
            return False

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
                cursor.execute(
                    'SELECT estoque FROM produto WHERE codigo_barras = %s', (codigo,))
                qnt_estoque = cursor.fetchone()[0]
                cursor.execute('UPDATE produto SET estoque = %s WHERE codigo_barras = %s', (float(
                    qnt) + float(qnt_estoque), codigo,))

                self.delete_window.lineEdit.setText('')
                self.delete_window.close()

        except ValueError:
            self.error_popup('A linha precisa ser um número inteiro.')

        finally:
            conn.commit()
            conn.close()

    # Função para abrir a janela de deletar produto da lista

    def keyPressEvent(self, event):

        if event.key() == QtCore.Qt.Key.Key_Enter and self.btn_confirmar.hasFocus():
            self.confirma_produto()

        if event.key() == QtCore.Qt.Key.Key_Return and self.btn_confirmar.hasFocus():
            self.confirma_produto()

        if event.key() == QtCore.Qt.Key.Key_Return and self.btn_finalizar_2.hasFocus():
            self.finaliza_compra()

        if event.key() == QtCore.Qt.Key.Key_Enter and self.btn_finalizar_2.hasFocus():
            self.finaliza_compra()

        if event.key() == QtCore.Qt.Key.Key_F10:
            self.delete_window.show()
            self.delete_window.error_msg.clicked.connect(
                self.deleta_produto_lista)

        if event.key() == QtCore.Qt.Key.Key_F11:
            self.finaliza_compra()

    # Função que trata o dado e valida se o código existe

    def valida_codigo(self, codigo,):

        conn, cursor = self.connection()

        try:
            int(codigo)
            cursor.execute(
                'SELECT * FROM produto WHERE codigo_barras = %s', (codigo,))
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
        cursor.execute(
            'SELECT estoque FROM produto WHERE codigo_barras = %s', (codigo,))
        qnt_estoque = cursor.fetchone()[0]

        try:
            float(qnt)

            if float(qnt) > qnt_estoque:
                self.error_popup('Quantidade indisponível.')

            else:
                cursor.execute("UPDATE produto SET estoque = %s WHERE codigo_barras = %s", (float(
                    qnt_estoque - float(qnt)), codigo,))
                return qnt

        except ValueError:
            self.error_popup('A quantidade precisa ser um número.')

        finally:
            conn.commit()
            conn.close()

    # Função é chamada para adicionar um produto na tabela de produtos

    def confirma_produto(self):
        self.payment_window.imprimir.setEnabled(False)
        self.payment_window.imprimir.setVisible(False)
        self.payment_window.confirmar_btn.setEnabled(True)
        self.payment_window.confirmar_btn.setVisible(True)

        try:
            codigo_produto = self.codigo_input.text()
            produto = self.valida_codigo(codigo_produto,)
            qnt_produto = self.qnt_input.text()
            qnt = self.valida_qnt(codigo_produto, qnt_produto)

            if produto and qnt:
                # Adicionando o produto na tabela de produtos
                rowPosition = self.tabela_produtos.rowCount()
                self.tabela_produtos.insertRow(rowPosition)
                self.tabela_produtos.setItem(
                    rowPosition-1, 0, QtWidgets.QTableWidgetItem(str(produto[0])))
                self.tabela_produtos.setItem(
                    rowPosition-1, 1, QtWidgets.QTableWidgetItem(produto[1]))
                self.tabela_produtos.setItem(
                    rowPosition-1, 2, QtWidgets.QTableWidgetItem(str(qnt)))
                preco = round(float(qnt)*produto[3], 2)
                self.precos.append(preco)
                self.tabela_produtos.setItem(
                    rowPosition-1, 3, QtWidgets.QTableWidgetItem(str(float(produto[3]))))
                self.tabela_produtos.setItem(
                    rowPosition-1, 4, QtWidgets.QTableWidgetItem(str(float(preco))))

                # Trocando o background das celulas
                self.tabela_produtos.item(
                    rowPosition-1, 0).setBackground(QtGui.QColor(243, 244, 245))
                self.tabela_produtos.item(
                    rowPosition-1, 1).setBackground(QtGui.QColor(243, 244, 245))
                self.tabela_produtos.item(
                    rowPosition-1, 2).setBackground(QtGui.QColor(243, 244, 245))
                self.tabela_produtos.item(
                    rowPosition-1, 3).setBackground(QtGui.QColor(243, 244, 245))
                self.tabela_produtos.item(
                    rowPosition-1, 4).setBackground(QtGui.QColor(243, 244, 245))

                # Alinhando eles no centro
                self.tabela_produtos.item(
                    rowPosition-1, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.tabela_produtos.item(
                    rowPosition-1, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.tabela_produtos.item(
                    rowPosition-1, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.tabela_produtos.item(
                    rowPosition-1, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.tabela_produtos.item(
                    rowPosition-1, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

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

            total = sum(self.precos)

            pagamento = self.payment_window.recebido_input.text()
            metodo_pagamento = self.payment_window.metodo_pagamento.currentText()
            metodo_desconto = self.payment_window.metodo_desconto.currentText()
            desconto = 0

            if metodo_desconto == '%' and self.payment_window.desconto_input.text() != '':
                desconto = float(
                    self.payment_window.desconto_input.text()) * total / 100

            elif metodo_desconto == 'R$' and len(self.payment_window.desconto_input.text()) > 0:
                desconto = float(self.payment_window.desconto_input.text())

            try:
                float(pagamento)
                if float(pagamento) < (total - desconto):
                    self.error_popup(
                        'O valor recebido é menor que o valor da compra')
                else:

                    troco = round(float(pagamento) - (total - desconto), 2)

                    if troco < 0 or desconto > total:
                        troco = 0

                    self.troco = troco
                    self.payment_window.total_valor_label_2.setText(
                        f'R${str(troco)}')

                    conn, cursor = self.connection()
                    metodo = self.payment_window.metodo_pagamento.currentText()
                    cursor.execute('INSERT INTO vendas (data, valor, metodo) VALUES (%s, %s, %s)', (
                        datetime.now(), float(total - desconto), metodo,))
                    conn.commit()
                    self.payment_window.imprimir.setEnabled(True)
                    self.payment_window.imprimir.setVisible(True)
                    self.payment_window.confirmar_btn.setEnabled(False)
                    self.payment_window.confirmar_btn.setVisible(False)

                    linhas_tabela = self.tabela_produtos.rowCount() - 1
                    # Exclui todas as linhas de produtos da tabela de produtos
                    for i in range(linhas_tabela):
                        self.itens.append([self.tabela_produtos.item(i, 0).text(), self.tabela_produtos.item(i, 1).text(), self.tabela_produtos.item(
                            i, 2).text(), self.tabela_produtos.item(i, 3).text(), self.tabela_produtos.item(i, 4).text()])

                    for i in range(linhas_tabela):
                        self.tabela_produtos.removeRow(0)

                    self.total = sum(self.precos)

                    # Retorna o valor de total para 0.00
                    self.total_label.setText('Total: R$0.00')

            except ValueError:
                self.error_popup('O valor recebido precisa ser um número.')

            except Exception as e:
                print(e, 'erro pagamento')

        self.payment_window.confirmar_btn.clicked.connect(troco)


class MainW(QMainWindow, MainWindow):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)

        self.label.setStyleSheet(
            'background-color: grey; font-size: 20px; font-weight: bold')
        self.label.setText('SUA LOGO AQUI')

        self.deletar_produto_janela = DeletarProduto()

        self.adicionar_item_janela = AdicionarItem()

        self.vendas_janela = GUI_cont()
        self.vendas_janela.close()

        self.estoque_janela = EstoqueWindow()

        self.editar_produto_janela = EditarProdutoWindow()

        self.pushButton.clicked.connect(self.vendas)
        self.pushButton_2.clicked.connect(self.adicionar_item_func)
        self.pushButton_5.clicked.connect(self.estoque)
        self.pushButton_4.clicked.connect(self.deletar_produto)
        self.pushButton_3.clicked.connect(self.editar_produto)

    def vendas(self):
        self.vendas_janela.show()

    def adicionar_item_func(self):
        self.adicionar_item_janela.show()

    def estoque(self):
        self.estoque_janela.show()

    def deletar_produto(self):
        self.deletar_produto_janela.show()

    def editar_produto(self):
        self.editar_produto_janela.show()


app = QApplication(sys.argv)
window = MainW()
window.show()
app.exec()
