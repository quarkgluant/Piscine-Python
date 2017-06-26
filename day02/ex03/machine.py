#!/usr/bin/env python3
# -*-coding:utf-8 -*-

import random
from beverages import *
class CoffeeMachine:
	"""la machine à café"""
	def __init__(self):
		self.count = 0

	class EmptyCup(HotBeverage):
		desc="An empty cup?! Gimme my money back!"
		def __init__(self, price = 0.90, name="empty cup"):
			HotBeverage.__init__(self, price, name)

	class BrokenMachineException(Exception):
		def __init__(self, msg= "This coffee machine has to be repaired."):
			Exception.__init__(self, msg)


	def serve(self, Klass):
		print ('use ', self.count)
		self.count += 1
		if self.count > 9:
			raise self.BrokenMachineException()
		return Klass() if random.randint(0, 1) == 0 else self.EmptyCup() 


	def repair(self):
		self.count = 0
		print ('***** et hop la machine machine again *****')


if __name__ == "__main__":
	for i in range(2):
		try:
			machine = CoffeeMachine()

			print(machine.serve(HotBeverage))
			print(machine.serve(Coffee))
			print(machine.serve(Coffee))
			print(machine.serve(Coffee))
			print(machine.serve(Tea))
			print(machine.serve(Tea))
			print(machine.serve(Cappuccino))
			print(machine.serve(Coffee))
			print(machine.serve(Tea))
			print(machine.serve(Tea))
			print(machine.serve(Cappuccino))
		except Exception as e:
			print(e)
			machine.repair()

