class Suhufi:
	def __init__(self,a):
		self.a = a
		
	def fahrenheit(self):
		return (self.a - 32) * 5/9

	def celcius(self):
		return (self.a * 9/5) + 32 

	def celKelvin(self):
		return self.a + 273.15

	def fahKelvin(self):
		return (self.a - 32) * 5/9 + 273.15 

	def kelvinCel(self):
		return self.a - 273.15

	def kelvinFah(self):
		return (self.a - 273.15) * 9/5 + 32