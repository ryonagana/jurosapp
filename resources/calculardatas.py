# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/calcularjuros.ui'
#
# Created: Sun Apr 21 18:20:18 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(503, 400)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cp_valor = QtGui.QDoubleSpinBox(Form)
        self.cp_valor.setMaximum(99999999.99)
        self.cp_valor.setObjectName("cp_valor")
        self.horizontalLayout.addWidget(self.cp_valor)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.cp_juros = QtGui.QDoubleSpinBox(Form)
        self.cp_juros.setMaximum(100.0)
        self.cp_juros.setSingleStep(2.0)
        self.cp_juros.setObjectName("cp_juros")
        self.horizontalLayout.addWidget(self.cp_juros)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.cp_diasatraso = QtGui.QSpinBox(Form)
        self.cp_diasatraso.setMaximum(999)
        self.cp_diasatraso.setObjectName("cp_diasatraso")
        self.horizontalLayout.addWidget(self.cp_diasatraso)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.cp_multa = QtGui.QDoubleSpinBox(Form)
        self.cp_multa.setMaximum(100.0)
        self.cp_multa.setObjectName("cp_multa")
        self.horizontalLayout.addWidget(self.cp_multa)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.bt_calcular = QtGui.QPushButton(Form)
        self.bt_calcular.setObjectName("bt_calcular")
        self.gridLayout.addWidget(self.bt_calcular, 1, 0, 1, 1)
        self.cp_tabela = QtGui.QTableView(Form)
        self.cp_tabela.setObjectName("cp_tabela")
        self.gridLayout.addWidget(self.cp_tabela, 3, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Valor:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Juros:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Dias de Atraso:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "% de Multa:", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_calcular.setText(QtGui.QApplication.translate("Form", "Calcular", None, QtGui.QApplication.UnicodeUTF8))

