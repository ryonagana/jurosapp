
import sys
import os
import datetime

from PySide2 import QtCore
from PySide2 import QtGui

from PySide2.QtWidgets import QWidget

from modules import calculoJuros

from PySide2.QtUiTools import QUiLoader


class calculoJurosWidget(QWidget):
	def __init__(self, parent = None):
		QWidget.__init__(self,None)
		
		self.widget = parent
		
		self.calcJuros = None
		
		self.connect()
		
	@QtCore.Slot()
	def calc(self):
		#print "kkkkkkk"
		
		valor = self.widget.cp_valor.value()
		juros = self.widget.cp_juros.value()
		atraso = self.widget.cp_diasatraso.value()
		multa = self.widget.cp_multa.value()
		
		
		self.calcJuros = calculoJuros.CalculoJuros(valor, juros, atraso, multa)
		
		model = QtGui.QStandardItemModel(3, 2, self)
		
		model.setHorizontalHeaderItem(0, QtGui.QStandardItem("Descricao"))
		model.setHorizontalHeaderItem(1, QtGui.QStandardItem("Valores"))

		self.calcJuros.calculaMulta(model)
		
		self.widget.cp_tabela.setModel(model)
		
		print (valor, juros, atraso, multa)
		
	
	def connect(self):
		self.widget.bt_calcular.clicked.connect(self.calc)