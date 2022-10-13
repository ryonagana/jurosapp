# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/jurossimples.ui'
#
# Created: Sun Apr 21 18:20:18 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(550, 400)
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 551, 381))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tbValores = QtGui.QTableView(self.gridLayoutWidget)
        self.tbValores.setObjectName("tbValores")
        self.gridLayout.addWidget(self.tbValores, 2, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)
        self.cpMeses = QtGui.QSpinBox(self.gridLayoutWidget)
        self.cpMeses.setMaximum(9999)
        self.cpMeses.setObjectName("cpMeses")
        self.gridLayout_2.addWidget(self.cpMeses, 1, 1, 1, 1)
        self.cpJuros = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.cpJuros.setMaximum(100.0)
        self.cpJuros.setObjectName("cpJuros")
        self.gridLayout_2.addWidget(self.cpJuros, 1, 2, 1, 1)
        self.cpCapital = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.cpCapital.setMaximum(99999999.99)
        self.cpCapital.setObjectName("cpCapital")
        self.gridLayout_2.addWidget(self.cpCapital, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.btCalcular = QtGui.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btCalcular.sizePolicy().hasHeightForWidth())
        self.btCalcular.setSizePolicy(sizePolicy)
        self.btCalcular.setObjectName("btCalcular")
        self.gridLayout.addWidget(self.btCalcular, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Capital:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Data em Meses:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Valor de Juros:", None, QtGui.QApplication.UnicodeUTF8))
        self.btCalcular.setText(QtGui.QApplication.translate("Form", "Calcular Juros Simples", None, QtGui.QApplication.UnicodeUTF8))

