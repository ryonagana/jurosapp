import sys,os
import datetime

import PySide2.QtGui
import PySide2.QtNetwork
import PySide2.QtXml

from PySide2 import QtCore
from PySide2 import QtGui

from PySide2.QtWidgets import QWidget, QCalendarWidget, QMessageBox

class calcDataWidget(QWidget):
	def __init__(self, window = None, parent = None):
		self.parent = parent
		self.ui = window
		
		self.connect()
		

		
		self.ui.cp_dataFim.setCalendarPopup(True)
		self.ui.cp_dataInicio.setCalendarPopup(True)
		
		calendarInicio = QCalendarWidget()
		calendarFim =    QCalendarWidget()
		
		self.ui.cp_dataInicio.setCalendarWidget(calendarInicio)
		self.ui.cp_dataFim.setCalendarWidget(calendarFim)
		
		
		self.ui.cp_dataInicio.setDate(datetime.datetime.now())
		self.ui.cp_dataFim.setDate(datetime.datetime.now())
		
		
	
	@QtCore.Slot()
	def calcdata(self):
		datainicio = self.ui.cp_dataInicio.date().toPython()
		datafim = self.ui.cp_dataFim.date().toPython()
		
		totaldias = (datafim - datainicio).days
		
		if totaldias == 0:
			QMessageBox.critical(None, "Erro: Data Invalida", "Insira a data corretamente")
			return
		
		
		mes = totaldias / 30
		
		anos = mes / 12
		
		if( (mes % 12) == 0):
			anos += 1
			mes = totaldias / anos
		
		
		str = "Resultado: Dias: %d\nMeses: %d\nAnos: %d\n" % (totaldias, mes, anos)
		
		self.ui.lb_resultado.setText(str)
			
		#print mes
		
	
	def connect(self):
		self.ui.bt_calc.clicked.connect(self.calcdata)
	
	
	