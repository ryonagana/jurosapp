from decimal import Decimal, getcontext


from PySide2 import QtGui
from PySide2 import QtWidgets




class CalculoJuros:
	def __init__(self, valor, juros, diasatraso, valormulta):
		self.valor = valor
		self.juros = juros
		self.atraso = diasatraso
		self.multa = valormulta
		
		self.multaconv = self.porcentagem(self.multa)
		self.jurosconv = self.porcentagem(self.juros)
	
	def porcentagem(self,pc):
		return (pc / 100)
		
	def pc_valor(self, valor,pc):
		porc = pc / 100
		
		return valor * porc
		
	def calculaMulta(self, model = None):
	
		getcontext().prec = 28
		
		if self.valor == 0.0:
			QtWidgets.QMessageBox.critical(None, "Erro: Valor Incorreto", "Por Favor Insira um valor Valido")
			return
		if self.juros == 0.0:
			QtWidgets.QMessageBox.critical(None,"Erro: Valor Incorreto", "Por Favor Coloque os Juros")
			return
			
		juros = Decimal(self.juros) / Decimal(30)
		porcJuros = Decimal(juros) * Decimal(self.atraso)
		porcMulta = Decimal(self.valor) * Decimal(self.porcentagem(self.juros))
		valorJuros = Decimal(self.valor) * Decimal(self.porcentagem(porcJuros))
		valorMulta = Decimal(self.valor)  * Decimal(self.porcentagem(self.multa))
		total = Decimal(valorJuros) + Decimal(valorMulta)
		resultado = Decimal(total) + Decimal(self.valor)
		
		if model != None:
		
			itempcMulta = QtGui.QStandardItem(f"{porcMulta:.2f}%")
			itempcJuros = QtGui.QStandardItem(f"{porcJuros:.2f}%")
			
			itemValorMulta = QtGui.QStandardItem(f"R$ {valorMulta:.2f}")
			itemValorJuros = QtGui.QStandardItem(f"R$ {valorJuros:.2f}")
			
			itemResultado  = QtGui.QStandardItem(f"R$ {resultado:.2f}")
			
			
			model.setItem(0,0,QtGui.QStandardItem("Porcentagem de Multa:"))
			model.setItem(1,0, QtGui.QStandardItem("Porcentagem de Juros:"))
			model.setItem(2,0,QtGui.QStandardItem("Valor de Multa:"))
			model.setItem(3,0, QtGui.QStandardItem("Valor de Juros:"))
			model.setItem(4,0, QtGui.QStandardItem("Total:"))
			
			model.setItem(0, 1, itempcMulta)
			model.setItem(1, 1, itempcJuros)
			model.setItem(2, 1, itemValorMulta)
			model.setItem(3, 1, itemValorJuros)
			model.setItem(4, 1, itemResultado)
		
		
		
		"""
		juros = (Decimal(self.juros) / Decimal(30)) * self.atraso

		print "Valor Juros: ", juros
		
		multas = [Decimal(self.valor) * Decimal(self.jurosconv),
				Decimal(self.valor) * Decimal(self.multaconv)]
				
		
		total = 0
		
		for m in multas:
			
			total += m
			
		
		print "Soma das multas ", total
		
		res = Decimal(total) + Decimal(self.valor)
		
		#print juros,self.jurosconv, multas, res
		
		if model != None:
		
			itemJuros = QtGui.QStandardItem("R$ %.2f" % juros)
			itemResultado = QtGui.QStandardItem("R$ %.2f" % res)
			
			model.setItem(0,0,QtGui.QStandardItem("Multa:"))
			model.setItem(1,0, QtGui.QStandardItem("Total:"))
			
			model.setItem(0,1,itemJuros)
			model.setItem(1,1,itemResultado)
			
			#for multa in multas:
				
			
			#model.setItem(0,0,"Valor : %.2f" % valor)
		"""
		
		
if __name__ == "__main__":
	a = CalculoJuros(119.80,9.8,18,5)
	a.calculaMulta()