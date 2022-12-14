# Form implementation generated from reading ui file 'estoque.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(880, 589)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(16777215, 589))
        Form.setStyleSheet("background-color: rgb(249, 249, 249);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setMinimumSize(QtCore.QSize(0, 70))
        self.frame.setStyleSheet("padding-left: 70%; padding-right: 70%;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border: 0px; background-color: rgb(238, 238, 238); ")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(12, 27, 37);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.frame)
        self.tabela_produtos = QtWidgets.QTableWidget(Form)
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
        self.tabela_produtos.setColumnCount(6)
        self.tabela_produtos.setRowCount(0)
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
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        item.setFont(font)
        self.tabela_produtos.setHorizontalHeaderItem(5, item)
        self.tabela_produtos.horizontalHeader().setCascadingSectionResizes(False)
        self.tabela_produtos.horizontalHeader().setDefaultSectionSize(121)
        self.tabela_produtos.horizontalHeader().setMinimumSectionSize(39)
        self.tabela_produtos.horizontalHeader().setSortIndicatorShown(True)
        self.verticalLayout.addWidget(self.tabela_produtos)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox.setItemText(0, _translate("Form", "C??digo"))
        self.comboBox.setItemText(1, _translate("Form", "Nome"))
        self.pushButton.setText(_translate("Form", "Pesquisar"))
        self.pushButton.setShortcut(_translate("Form", "Return"))
        item = self.tabela_produtos.horizontalHeaderItem(0)
        item.setText(_translate("Form", "C??digo"))
        item = self.tabela_produtos.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Produto"))
        item = self.tabela_produtos.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Categoria"))
        item = self.tabela_produtos.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Pre??o"))
        item = self.tabela_produtos.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Quantidade"))
        item = self.tabela_produtos.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Marca"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
