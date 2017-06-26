#!/usr/bin/env python3
# -*-coding:utf-8 -*

def my_var():
	""" Affiche le type d'une liste d'arguments
	# 42 est de type type(42)
	# 42 est de type <class 'str'>
	# quarante-deux est de type <class 'str'>
	# 42.0 est de type <class 'float'>
	# True est de type <class 'bool'>
	# [42] est de type <class 'list'>
	# {42: 42} est de type <class 'dict'>
	# (42,) est de type <class 'tuple'>
	# set() est de type <class 'set'> """
	for elem in [42, "42", "quarante-deux", 42.0, True, [42], {42: 42}, (42,), set()]:
		print("{0} est de type {1}".format(elem, type(elem)))

if __name__ == '__main__':
    my_var()