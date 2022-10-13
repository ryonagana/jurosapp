import sys

from PySide2 import QtGui


class JurosSimples:
	def __init__(self,valor, data, juros, parent = None):
		self.valor = valor
		self.data = data
		self.juros = self.calculaJuros(juros)
		
		self.mainwindow = parent
		

		
		print ("round no juros simples ", self.mainwindow.round)
		
		#self.formula
		
	
	def calculaJuros(self,juros):
		
		val = self.valor * (juros / 100)
		return val
		
	def geraTabela(self, model):
		
		capital = self.valor
		
		for mes in range(self.data):
			
			auxcap = capital + self.juros
			capital =  auxcap
			
			novocapital = capital - self.juros
			
			print ("Juros Simples Arrendondado?", self.mainwindow.round )
			
			if self.mainwindow.round == True:
				itemJuros = QtGui.QStandardItem("R$ %.2f" % round(self.juros,1))
				itemCapital = QtGui.QStandardItem("R$ %.2f" % round(novocapital,1))
				itemMont = QtGui.QStandardItem("R$ %.2f" % round(auxcap,1))
			elif self.mainwindow.round == False:
				itemJuros = QtGui.QStandardItem("R$ %.2f" % self.juros)
				itemCapital = QtGui.QStandardItem("R$ %.2f" % novocapital)
				itemMont = QtGui.QStandardItem("R$ %.2f" % auxcap)	
			
			
			model.setItem(mes,0,itemCapital)
			model.setItem(mes,1,itemJuros)
			model.setItem(mes,2,itemMont)
			
			print ("R$ %.2f  R$ %.2f  R$ %.2f" % (capital,self.juros,auxcap))
			
			
	
	
	
if __name__ == "__main__":
	app = JurosSimples(12600,6,6.00)
	app.geraTabela(None)
		
		