# -*- coding: utf-8 -*-
'''
Created on 09/12/2012

@author: Mastermind
'''

import sys
import os
import datetime

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2.QtWidgets import QWidget

from modules import DescontoRacional, DescontoRacionalComposto

from PySide2.QtUiTools import QUiLoader

class DescontosWidget(QWidget):
		
		def __init__(self, widget = None, mainwindow = None):
			QWidget.__init__(self,None)
			
			self.parent = widget
			self.mainwindow = mainwindow
			
			self.dr = None
			self.drc = None
			
			self.connect()
			
		
		@QtCore.Slot()
		def calc_dr(self):
			
			valor = self.parent.cp_drvalor.value()
			
			juros = self.parent.cp_drjuros.value()
			
			meses = self.parent.cp_drmeses.value()
			
			print (valor,juros,meses)
			
			self.dr = DescontoRacional.DescontoRacional(valor,juros,meses)
			
			if self.mainwindow.round == True:
				total = round(self.dr.calcularDrc(),4)
			else:
				total = self.dr.calcularDrc()
			
			data = "Resultado Desconto Racional: R$ %.2f" % total
			self.parent.lb_dr_resultado.setText(data)
			
		
		@QtCore.Slot()
		def calc_drc(self):
			valor = self.parent.cp_drcvalor.value()
			
			juros = self.parent.cp_drcjuros.value()
			
			meses = self.parent.cp_drcmeses.value()
			
			print (valor,juros,meses)
			
			self.dr = DescontoRacionalComposto.DescontoRacionalComposto(valor,juros,meses)
			
			if self.mainwindow.round == True:
				total = round(self.dr.calcDrc(),4)
			else:
				total = self.dr.calcDrc()
			
			data = u"Resultado Desconto Racional: R$ %.2f" % total
			self.parent.lb_drc_resultado.setText(data)
		
		def connect(self):
			
			self.parent.bt_drcalc.clicked.connect(self.calc_dr)
			self.parent.bt_drccalc.clicked.connect(self.calc_drc)