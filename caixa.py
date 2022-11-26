# Form implementation generated from reading ui file 'caixa.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 716)
        MainWindow.setMinimumSize(QtCore.QSize(0, 716))
        MainWindow.setMaximumSize(QtCore.QSize(1366, 716))
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("background-color: rgb(249, 249, 249);")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main_body = QtWidgets.QFrame(self.widget)
        self.main_body.setMinimumSize(QtCore.QSize(700, 0))
        self.main_body.setMaximumSize(QtCore.QSize(700, 650))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        self.main_body.setFont(font)
        self.main_body.setStyleSheet("border: 0px;\n"
"")
        self.main_body.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main_body.setObjectName("main_body")
        self.btn_confirmar = QtWidgets.QPushButton(self.main_body)
        self.btn_confirmar.setGeometry(QtCore.QRect(310, 410, 231, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        self.btn_confirmar.setFont(font)
        self.btn_confirmar.setAutoFillBackground(False)
        self.btn_confirmar.setStyleSheet("background-color: rgb(12, 27, 37);\n"
"color: rgb(255, 255, 255);")
        self.btn_confirmar.setCheckable(False)
        self.btn_confirmar.setChecked(False)
        self.btn_confirmar.setAutoRepeatDelay(300)
        self.btn_confirmar.setAutoRepeatInterval(3)
        self.btn_confirmar.setObjectName("btn_confirmar")
        self.qnt_label = QtWidgets.QLabel(self.main_body)
        self.qnt_label.setGeometry(QtCore.QRect(100, 310, 118, 27))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(15)
        self.qnt_label.setFont(font)
        self.qnt_label.setStyleSheet("")
        self.qnt_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.qnt_label.setObjectName("qnt_label")
        self.codigo_label = QtWidgets.QLabel(self.main_body)
        self.codigo_label.setEnabled(True)
        self.codigo_label.setGeometry(QtCore.QRect(120, 220, 72, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.codigo_label.sizePolicy().hasHeightForWidth())
        self.codigo_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(15)
        self.codigo_label.setFont(font)
        self.codigo_label.setStyleSheet("")
        self.codigo_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.codigo_label.setObjectName("codigo_label")
        self.codigo_input = QtWidgets.QLineEdit(self.main_body)
        self.codigo_input.setGeometry(QtCore.QRect(270, 220, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.codigo_input.setFont(font)
        self.codigo_input.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.codigo_input.setText("")
        self.codigo_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.codigo_input.setObjectName("codigo_input")
        self.qnt_input = QtWidgets.QLineEdit(self.main_body)
        self.qnt_input.setGeometry(QtCore.QRect(270, 300, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.qnt_input.setFont(font)
        self.qnt_input.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.qnt_input.setText("")
        self.qnt_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.qnt_input.setObjectName("qnt_input")
        self.horizontalLayout.addWidget(self.main_body)
        self.produtos = QtWidgets.QFrame(self.widget)
        self.produtos.setEnabled(True)
        self.produtos.setMinimumSize(QtCore.QSize(500, 0))
        self.produtos.setMaximumSize(QtCore.QSize(1100, 650))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.produtos.setFont(font)
        self.produtos.setStyleSheet("border: 0px;\n"
"")
        self.produtos.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.produtos.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.produtos.setObjectName("produtos")
        self.label_logo = QtWidgets.QLabel(self.produtos)
        self.label_logo.setGeometry(QtCore.QRect(9, 9, 631, 60))
        self.label_logo.setMinimumSize(QtCore.QSize(0, 60))
        self.label_logo.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_logo.setFont(font)
        self.label_logo.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_logo.setStyleSheet("background-color: rgb(10, 78, 223);")
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        self.tabela_produtos = QtWidgets.QTableWidget(self.produtos)
        self.tabela_produtos.setGeometry(QtCore.QRect(9, 75, 631, 491))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(15)
        font.setKerning(True)
        self.tabela_produtos.setFont(font)
        self.tabela_produtos.setStyleSheet("border: 1px solid rgb(239,239,239);\n"
"")
        self.tabela_produtos.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.tabela_produtos.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tabela_produtos.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tabela_produtos.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tabela_produtos.setAlternatingRowColors(True)
        self.tabela_produtos.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerItem)
        self.tabela_produtos.setShowGrid(True)
        self.tabela_produtos.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.tabela_produtos.setObjectName("tabela_produtos")
        self.tabela_produtos.setColumnCount(5)
        self.tabela_produtos.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_produtos.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        item.setFont(font)
        item.setBackground(QtGui.QColor(243, 244, 245))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.tabela_produtos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        item.setFont(font)
        self.tabela_produtos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        item.setFont(font)
        self.tabela_produtos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        item.setFont(font)
        self.tabela_produtos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        item.setFont(font)
        self.tabela_produtos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_produtos.setItem(0, 3, item)
        self.tabela_produtos.horizontalHeader().setCascadingSectionResizes(False)
        self.tabela_produtos.horizontalHeader().setDefaultSectionSize(121)
        self.tabela_produtos.horizontalHeader().setMinimumSectionSize(39)
        self.tabela_produtos.horizontalHeader().setSortIndicatorShown(True)
        self.total_label = QtWidgets.QLabel(self.produtos)
        self.total_label.setGeometry(QtCore.QRect(250, 570, 151, 27))
        self.total_label.setMinimumSize(QtCore.QSize(0, 27))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        self.total_label.setFont(font)
        self.total_label.setAutoFillBackground(False)
        self.total_label.setStyleSheet("background-color: rgb(12, 27, 37);\n"
"color: rgb(255, 255, 255);")
        self.total_label.setMidLineWidth(0)
        self.total_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.total_label.setIndent(-1)
        self.total_label.setObjectName("total_label")
        self.btn_finalizar_2 = QtWidgets.QPushButton(self.produtos)
        self.btn_finalizar_2.setGeometry(QtCore.QRect(227, 610, 191, 27))
        self.btn_finalizar_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        self.btn_finalizar_2.setFont(font)
        self.btn_finalizar_2.setAutoFillBackground(False)
        self.btn_finalizar_2.setStyleSheet("background-color: rgb(0, 166, 90);")
        self.btn_finalizar_2.setObjectName("btn_finalizar_2")
        self.horizontalLayout.addWidget(self.produtos)
        MainWindow.setCentralWidget(self.widget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1366, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuEstoque = QtWidgets.QMenu(self.menuBar)
        self.menuEstoque.setObjectName("menuEstoque")
        self.menuRegistro = QtWidgets.QMenu(self.menuBar)
        self.menuRegistro.setObjectName("menuRegistro")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAdicionar_produto_ao_estoqeu = QtGui.QAction(MainWindow)
        self.actionAdicionar_produto_ao_estoqeu.setObjectName("actionAdicionar_produto_ao_estoqeu")
        self.actionEditar_item_no_estoque = QtGui.QAction(MainWindow)
        self.actionEditar_item_no_estoque.setObjectName("actionEditar_item_no_estoque")
        self.actionRemover_item_do_estoque = QtGui.QAction(MainWindow)
        self.actionRemover_item_do_estoque.setObjectName("actionRemover_item_do_estoque")
        self.actionVer_estoque = QtGui.QAction(MainWindow)
        self.actionVer_estoque.setObjectName("actionVer_estoque")
        self.actionVendas = QtGui.QAction(MainWindow)
        self.actionVendas.setObjectName("actionVendas")
        self.menuEstoque.addAction(self.actionAdicionar_produto_ao_estoqeu)
        self.menuEstoque.addAction(self.actionEditar_item_no_estoque)
        self.menuEstoque.addAction(self.actionRemover_item_do_estoque)
        self.menuEstoque.addAction(self.actionVer_estoque)
        self.menuRegistro.addAction(self.actionVendas)
        self.menuBar.addAction(self.menuEstoque.menuAction())
        self.menuBar.addAction(self.menuRegistro.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.codigo_input, self.qnt_input)
        MainWindow.setTabOrder(self.qnt_input, self.btn_confirmar)
        MainWindow.setTabOrder(self.btn_confirmar, self.btn_finalizar_2)
        MainWindow.setTabOrder(self.btn_finalizar_2, self.tabela_produtos)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_confirmar.setText(_translate("MainWindow", "CONFIRMAR PRODUTO"))
        self.qnt_label.setText(_translate("MainWindow", "QUANTIDADE"))
        self.codigo_label.setText(_translate("MainWindow", "CÓDIGO"))
        item = self.tabela_produtos.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tabela_produtos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Código"))
        item = self.tabela_produtos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Produto"))
        item = self.tabela_produtos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantidade"))
        item = self.tabela_produtos.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Valor Unitário"))
        item = self.tabela_produtos.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Valor Total"))
        __sortingEnabled = self.tabela_produtos.isSortingEnabled()
        self.tabela_produtos.setSortingEnabled(False)
        self.tabela_produtos.setSortingEnabled(__sortingEnabled)
        self.total_label.setText(_translate("MainWindow", "Total: R$00.00"))
        self.btn_finalizar_2.setText(_translate("MainWindow", "FINALIZAR VENDA"))
        self.btn_finalizar_2.setShortcut(_translate("MainWindow", "F11"))
        self.menuEstoque.setTitle(_translate("MainWindow", "Estoque"))
        self.menuRegistro.setTitle(_translate("MainWindow", "Registro"))
        self.actionAdicionar_produto_ao_estoqeu.setText(_translate("MainWindow", "Adicionar produto ao estoque"))
        self.actionEditar_item_no_estoque.setText(_translate("MainWindow", "Editar item no estoque"))
        self.actionRemover_item_do_estoque.setText(_translate("MainWindow", "Remover item do estoque"))
        self.actionVer_estoque.setText(_translate("MainWindow", "Ver estoque"))
        self.actionVendas.setText(_translate("MainWindow", "Vendas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
