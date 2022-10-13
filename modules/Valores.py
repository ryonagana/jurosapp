'''
Created on 03/11/2012

@author: Mastermind
'''
import sys
import json
from PySide2 import QtCore
from PySide2 import QtGui
import datetime

class Valores:
	def __init__(self, window):
		
		self.window = window
		self.cpValor = window.cpValor.value()
		self.cpData =  (window.cpDataFim.date().toPython() - window.cpDataInicio.date().toPython()).days / 30
		self.cpJuros = window.cpJuros.value()
		
		
		
	def write(self, jsonfile):
			
		f = open(jsonfile,"wb")
			
		data = {'valor': self.cpValor, 'data' : self.cpData, 'juros': self.cpJuros }
			
		json.dump(data, f)
			
		f.flush()
		f.close()
		
		
	def openVal(self,jsonfile):
		
		filedata = None
		
		with open(jsonfile,"rb") as f:
			
			try:
				filedata = json.loads(f.read())
			except Exception as msg:
				print (msg)
				
			self.window.cpValor.setValue(filedata["valor"])
			self.window.cpJuros.setValue(filedata["juros"])
			
			
			#nao tem como pegar os meses que foram salvos e sim a diferenca
			#entao quand carregado  sempre vaiser hoje + diferenca
			
			data = QtCore.QDate( datetime.datetime.now() + datetime.timedelta(days=filedata["data"] * 30))
			
			self.window.cpDataFim.setDate(data)
			
			
		
		