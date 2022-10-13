'''
Created on 29/10/2012

@author: Mastermind
'''

import sys
import os
import datetime


from PySide2 import QtCore
from PySide2 import QtGui


from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QTextCodec

import JurosSimplesWidget
import calculoJurosWidget
import DescontosWidget
import calcDataWidget

from modules import JurosCompostos, Valores, JurosSimples, calculoJuros,Config
from modules import DescontoRacional, DescontoRacionalComposto

from PySide2.QtWidgets import QApplication, QCalendarWidget, QMessageBox

class MainApp(QApplication):
	def __init__(self):
			QApplication.__init__(self, sys.argv)
			self.codec = QTextCodec.codecForName("UTF-8")
			
			self.pack  = None
			self.res_modules = {}

			self.uiLoader = QUiLoader()
			self.window = self.uiLoader.load("resources/mainwindow.ui",None)
			self.window.about = self.uiLoader.load("resources/about.ui",None)
			self.window.jurossimples = self.uiLoader.load("resources/jurossimples.ui",None)
			self.window.calcjuros = self.uiLoader.load("resources/calcularjuros.ui",None)
			self.window.descontos = self.uiLoader.load("resources/descontos.ui",None)
			self.window.calcData = self.uiLoader.load("resources/calculardatas.ui",None)
			
			
			self.round = False
			
			self.configInstance = Config.Config("config.cfg")
			


			self.isResultGenerated = False
			self.descontosWidget = DescontosWidget.DescontosWidget(self.window.descontos, self)
			self.JurosSimplesWidget =  JurosSimplesWidget.JurosSimplesWidget(self.window.jurossimples, self)
			self.calcularJurosWidget =  calculoJurosWidget.calculoJurosWidget(self.window.calcjuros)
			self.calcDataWidget = calcDataWidget.calcDataWidget(self.window.calcData,self)
			self.jurosComposto = None
		
			self.define()
			self.connect()
	
	
	
	def checkResult(self):
		if not self.isResultGenerated:
			#print "No Result was Generated\n Nenhum Resultado foi gerado"
			return False
		
		return True
	
	def define(self):
		self.window.cpDataInicio.setDate( datetime.datetime.now())
		self.window.cpDataFim.setDate( datetime.datetime.now())
		
		self.window.cpDataInicio.setCalendarPopup(True)
		self.window.cpDataFim.setCalendarPopup(True)
		
		
		self.window.lbFormula.setText("")
		
		#test mode
		#self.window.cpDataInicio.setDate( datetime.datetime.now())
		#self.window.cpDataFim.setDate( datetime.date(2013,02,04))
		
		#self.window.cpValor.setValue(7000)
		#self.window.cpJuros.setValue(5.00)
		
		self.v = Valores.Valores(self.window)
		self.window.tbCalculos.addTab(self.window.jurossimples,"Juros Simples")
		self.window.tbCalculos.addTab(self.window.calcjuros,"Calculos de Juros (Boleto)")
		self.window.tbCalculos.addTab(self.window.descontos, "Calculos de Descontos")
		
		#self.window.tbCalculos.addWidget(self.window.jurosSimples)
		
		
		calendarInicio = QCalendarWidget()
		calendarFim =  QCalendarWidget()
		self.window.cpDataFim.setCalendarWidget(calendarInicio)
		self.window.cpDataInicio.setCalendarWidget(calendarFim)
			
	def run(self):
		
		self.window.showNormal()
		sys.exit(self.exec_())
		
	@QtCore.Slot()
	def calculaJuros(self):
		
		
		valor =  self.window.cpValor.value()
		data_inicio = self.window.cpDataInicio.date().toPython()
		data_fim = self.window.cpDataFim.date().toPython()
		juros = self.window.cpJuros.value()
		
		#works :)
		
		#if( data_fim <= data_inicio):
		#	print "Erro Data de Inicio maior que vencimento"
		#	return
		
		months = (data_fim - data_inicio).days // 30
		
		if (months == 0):
			#print "Erro Mes Negativo ou igual a Zero"
			QMessageBox.critical(None, "Erro: Data Inválida", "Por favor selecione a data corretamente")
			return
			
		elif(months < 0):
			#print "Erro Mes Negativo ou igual a Zero"
			QMessageBox.critical(None, "Erro: Data Invalida", "O Campo data � invalido, Por Favor Tente colocar um valor corretamente")
			return
		
		#print months
		
		self.jurosComposto = JurosCompostos.JurosComposto(valor, juros, months, self)
		
		valorFormula = "Valor da Formula :" +  " R$ %.2f" % self.jurosComposto.valor
		self.window.lbFormula.setText(valorFormula)
		
		
		#generate table
		
		model = QtGui.QStandardItemModel(months,3, self)
		
		model.setHorizontalHeaderItem(0, QtGui.QStandardItem("Capital"))
		model.setHorizontalHeaderItem(1, QtGui.QStandardItem("Juros"))
		model.setHorizontalHeaderItem(2, QtGui.QStandardItem("Montante"))
		self.jurosComposto.gerarTabela(model)
		
		
		self.window.cpTabela.setModel(model)
		self.isResultGenerated = True
		
	@QtCore.Slot()
	def about(self):
		
			self.window.about.exec_()
		
	@QtCore.Slot()
	def okAbout(self):
		self.window.about.close()
		
	@QtCore.Slot()
	def QtLicense(self):
		self.aboutQt()
	
	
	@QtCore.Slot()
	def salvarResultado(self):
		if not self.isResultGenerated:
			#print "Nao pode salvar resultado nao existe"
			return
		
		data = ""
		
	
		for linha in self.jurosComposto.tabela:
			
			
			capital = f"{linha[0]:.2f}"
			juros = f"{linha[1]:.2f}"
			montante = f"{linha[2]:.2f}"
			
			data += capital + " " + juros + " " + montante + "\n"
			
			
			
			
		save,filetype = QtGui.QFileDialog.getSaveFileName(None,"Salvar Resultado", "C:\\","Arquivo de Texto (*.txt)")
		
		f = open(save,"wb")
		#print save
		
		f.write(data)
		
		f.flush()
		f.close()
	
	@QtCore.Slot()
	def salvarValores(self):
		
		if not self.checkResult():
			return 
		
		save,filetype = QtGui.QFileDialog.getSaveFileName(None,"Salvar Resultado", "C:\\", "Val Files (*.val)")
		
		
		self.v.write(save)
	
	@QtCore.Slot()
	def lerValores(self):
		#if not self.checkResult():
		#	return
		
		open,filetype = QtGui.QFileDialog.getOpenFileName(None,"Abrir Resultado", "C:\\", "Val Files (*.val)")
		
		self.v.openVal(open)
	
	@QtCore.Slot()
	def menuRoundValues(self):
		
		self.configInstance.writecfg(self.window.acRoundValues.isChecked())
		self.configInstance.read()
		
		#self.config = self.configInstance.getConfig()
		self.round = False
	
	@QtCore.Slot()	
	def quit(self):
		self.window.close()
	
	
	@QtCore.Slot()
	def calculaData(self):
		self.window.calcData.show()
	
		
	def connect(self):
		
		#child windows actions
		self.window.about.btOkAbout.clicked.connect(self.okAbout)
		
		#main window actions
		
		self.window.acLerValores.triggered.connect(self.lerValores)
		self.window.acSalvarValores.triggered.connect(self.salvarValores)
		self.window.acSalvarResultado.triggered.connect(self.salvarResultado)
		self.window.btCalculaJuros.clicked.connect(self.calculaJuros)
		self.window.acSobre.triggered.connect(self.about)
		self.window.acRoundValues.triggered.connect(self.menuRoundValues)
		self.window.acQT.triggered.connect(self.QtLicense)
		self.window.acSair.triggered.connect(self.quit)
		self.window.acCalcData.triggered.connect(self.calculaData)
	
if __name__ == "__main__":
	app = MainApp()
	
	app.run()
	
