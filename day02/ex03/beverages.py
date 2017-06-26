#!/usr/bin/env python3
# -*-coding:utf-8 -*-

class HotBeverage:
	"""fait une boisson chaude"""
	desc="Just some hot water in a cup."
	def __init__(self, price = 0.30, name = "hot beverage"):
		self.price = price
		self.name = name

	def __str__(self):
		return self.Name

	@property
	def description(self):
		return self.desc

	def __str__(self):
		return "name : {0}\nprice : {1}\ndescription : {2}".format(self.name, '%.2f' %self.price, self.description)

class Coffee(HotBeverage):
	"""cafe"""
	desc="A coffee, to stay awake."
	def __init__(self, price = 0.40, name="coffee"):
		HotBeverage.__init__(self, price, name)

class Tea(HotBeverage):
	"""the"""
	desc="Just some hot water in a cup."
	def __init__(self, price = 0.30, name="tea"):
		 HotBeverage.__init__(self, price, name)

class Chocolate(HotBeverage):
	"""chocolat"""
	desc="Chocolate, sweet chocolate..."
	def __init__(self, price = 0.50,name="chocolate"):
		HotBeverage.__init__(self, price, name) 

class Cappuccino(HotBeverage):
	"""cappuccino"""
	desc="Un po' di Italia nella sua tazza!"
	def __init__(self, price = 0.45, name="cappuccino"):
		HotBeverage.__init__(self, price, name) 




if __name__ == "__main__":
	boisson_chaude = HotBeverage()
	print (boisson_chaude)
	cafe = Coffee()
	print (cafe)
	the = Tea()
	print (the)
	choco = Chocolate()
	print (choco)
	cappu = Cappuccino()
	print (cappu)