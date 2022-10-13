import sys
import math

from PySide2 import QtGui


class JurosComposto:
	def __init__(self, capital, juros, meses, parent = None):
		
		self.capital = capital
		self.juros = self.converterJuros(juros)
		self.meses = meses
		self.valor = self.calculaFormula()
		
		self.mainwindow = parent
		
		self.tabela = []
		
	
	def converterJuros(self,juros):
		return juros / 100
	
	def calculaFormula(self):
		
		val = self.capital * ( 1 + ( self.juros)) ** self.meses
		

		return val

	
	def  calcJuros(self, capital, juros):
		aux = juros * capital
		return aux
		

	def gerarTabela(self, model):
		
		print(f"MESES: {self.meses}")
		capital = self.capital
		
		for mes in range(self.meses):
			
			lista = []
			
			
			
			
			
			juros = self.juros * capital
			auxcap = capital + juros
			capital = auxcap
			
			
			lista = [capital, juros, auxcap]
			self.tabela.append(lista)
			print ("Arrendondamento ",self.mainwindow.round)
			if (self.mainwindow.round == True):
				itemJuros = QtGui.QStandardItem("R$ %.2f" % math.ceil(round(juros,2)))
				itemCapital = QtGui.QStandardItem("R$ %.2f" % math.ceil(round(capital,2)))
				itemMontante = QtGui.QStandardItem( "R$ %.2f" % math.ceil(round(auxcap,2)))
			elif (self.mainwindow.round == False):
				itemJuros = QtGui.QStandardItem("R$ %.2f" % juros)
				itemCapital = QtGui.QStandardItem("R$ %.2f" % capital)
				itemMontante = QtGui.QStandardItem( "R$ %.2f" % auxcap )
			
		
			model.setItem(mes,0,itemCapital)
			model.setItem(mes,1,itemJuros)
			model.setItem(mes,2,itemMontante)

