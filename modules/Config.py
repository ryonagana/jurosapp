import json
import os, sys

class Config:
	def __init__(self, filepath):
		self.path = os.path.abspath(filepath)
		
		self.data = None
		
		try:
			with open(self.path,"r") as f:
				self.data = json.load(f, encoding="utf-8")
			
		except Exception as msg:
			#print "File Not Found:"
			#print "Exception at: ", msg
			f = open("config.cfg","w")
			
			data = {"Round Values":"True"}
			
			json.dump(data,f)
			
			f.flush()
			f.close()
			
			self.read()
	
	def read(self):
	
		try:
			with open(self.path,"rb") as f:
				self.data = json.load(f, encoding="utf-8")
		except FileNotFoundError as fex:
			print ("File Not Found!")
			pass
		
		
	def writecfg(self, value):
		
		with open(self.path,"w") as wf:
			
			if value == True:	
				self.data["Round Values"] = "True"
			elif value == False:
				self.data["Round Values"] = "False"
			else:
				self.data["Round Values"] = "False"
			
			json.dump(self.data,wf)
			
		
	@staticmethod
	def getConfig(self):
		
		if self.data != None:
			return self.data
		
		return 0
		

