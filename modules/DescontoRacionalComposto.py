'''
Created on 09/12/2012

@author: Mastermind
'''
class DescontoRacionalComposto:
		def __init__ (self, valor, juros, meses, parent = None):
				self.mainwindow = parent
				
				self.valor = valor
				self.juros = juros
				self.meses = meses
				
		def porcentagem(self,val):
				return val / 100
				
		def calcDrc(self):
			

			calcpar = ((self.porcentagem(self.juros)) + 1) ** self.meses
			
			print ("Parenteses ", calcpar)
			
			calccolch = self.valor / calcpar
			
			print ("Colchetes ", calccolch)
			
			
			calcchaves  = self.valor - calccolch
			
			print ("Chaves ", calcchaves)
			
			return calcchaves
			
			
if __name__ == "__main__":
		a = DescontoRacionalComposto(10000.00,4.00,2)
		a.calcDrc()