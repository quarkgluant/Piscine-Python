#!/usr/bin/env python3
# -*-coding:utf-8 -*

def my_sort():
	d = {
	'Hendrix' : '1942',
	'Allman' : '1946',
	'King' : '1925',
	'Clapton' : '1945',
	'Johnson' : '1911',
	'Berry' : '1926',
	'Vaughan' : '1954',
	'Cooder' : '1947',
	'Page' : '1944',
	'Richards' : '1943',
	'Hammett' : '1962',
	'Cobain' : '1967',
	'Garcia' : '1942',
	'Beck' : '1944',
	'Santana' : '1947',
	'Ramone' : '1948',
	'White' : '1975',
	'Frusciante': '1970',
	'Thompson' : '1949',
	'Burton' : '1939',
	}
	def tri(nom_et_annee):
		return (nom_et_annee[1], nom_et_annee[0])

	liste = sorted(d.items(), key=tri)
	for artiste, annee in liste:
		print (artiste)



if __name__ == '__main__':
    my_sort()
    