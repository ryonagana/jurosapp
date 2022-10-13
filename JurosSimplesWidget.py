# -*- coding: utf-8 -*-
import sys,os
import datetime

import PySide2.QtGui
import PySide2.QtNetwork
import PySide2.QtXml

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2.QtWidgets import QWidget

from modules import JurosSimples

from PySide2.QtUiTools import QUiLoader

class JurosSimplesWidget(QWidget):
	def __init__(self, ui = None, parent = None):
		QWidget.__init__(self,None)
		self.widget = ui
		self.parent = parent
		
		self.jurosClass = None
		
		self.isResultGenerated = False
		
		
		
		self.define()
		self.connect()
	
	@QtCore.Slot()
	def calcular(self):
		
		valor = self.widget.cpCapital.value()
		data = self.widget.cpMeses.value()
		juros = self.widget.cpJuros.value()
		
		print (valor,data,juros)
		
		
		if data <= 0:
			QtGui.QMessageBox.critical(None, "Erro: Data Invalida", "O Campo data e invalido, Por Favor Tente colocar um valor corretamente")
			return
			
			 
		self.jurosClass = JurosSimples.JurosSimples(valor,data,juros, self.parent)
		self.isResultGenerated = True
		
		
		
		model = QtGui.QStandardItemModel(data,3, self)
		
		model.setHorizontalHeaderItem(0, QtGui.QStandardItem("Capital"))
		model.setHorizontalHeaderItem(1, QtGui.QStandardItem("Juros"))
		model.setHorizontalHeaderItem(2, QtGui.QStandardItem("Montante"))
		
		self.jurosClass.geraTabela(model)
		
		self.widget.tbValores.setModel(model)
		
	
	def define(self):
		pass
	
	def connect(self):
		self.widget.btCalcular.clicked.connect(self.calcular)
