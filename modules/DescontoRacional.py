import sys

from PySide2 import QtGui


class DescontoRacional:
	def __init__(self, valor, juros, meses, parent = None):
		
		self.mainwindow = parent
		self.valor = valor
		self.juros = juros
		self.meses = meses
		
	def porcentagem(self,val):
			return val / 100
		
	def calcularDrc(self):
		
		valor = 1 + self.porcentagem(self.juros)  * self.meses
		
		dr = self.valor / valor
		
		total = self.valor - dr
		
		
		
		return total
		
		
		
if __name__ == "__main__":
	app = DescontoRacional(10000.00,4.00,2)
	app.calcularDrc()