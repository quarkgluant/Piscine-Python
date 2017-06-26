#!/usr/bin/env python3
# -*-coding:utf-8 -*

def numbers():
	""" affiche le contenu du fichier numbers.txt, un chiffre par ligne """
	with open("numbers.txt", "r") as mon_fichier:
		contenu = mon_fichier.read().split(",")
		for elem in contenu:
			print(elem.strip())

if __name__ == '__main__':
	numbers()