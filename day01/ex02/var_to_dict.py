#!/usr/bin/env python3
# -*-coding:utf-8 -*

def var_to_dyc():
	""" transforme une liste de liste en dictionnaire puis l'affiche"""
	d = [
		('Hendrix'      , '1942'),
		('Allman'       , '1946'),
		('King'         , '1925'),
		('Clapton'      , '1945'),
		('Johnson'      , '1911'),
		('Berry'        , '1926'),
		('Vaughan'      , '1954'),
		('Cooder'       , '1947'),
		('Page'         , '1944'),
		('Richards'     , '1943'),
		('Hammett'      , '1962'),
		('Cobain'       , '1967'),
		('Garcia'       , '1942'),
		('Beck'         , '1944'),
		('Santana'      , '1947'),
		('Ramone'       , '1948'),
		('White'        , '1975'),
		('Frusciante'   , '1970'),
		('Thompson'     , '1949'),
		('Burton'       , '1939')
	]
	# inverted_dict = dict([[v, k] for k, v in mydict.items()])
	# DictInvert = lambda d: dict(zip(d.values(), d.keys()))
	mon_dictionnaire_invers = {}
	for v, k in d:
		# print("{} et {}".format(k, v))
		mon_dictionnaire_invers[v] = k
	mon_dictionnaire = {}
	for k, v in mon_dictionnaire_invers.items():
		keys = mon_dictionnaire.setdefault(v, [])
		keys.append(k)
	# dico = {k: v for k, v in d}
	# print(mon_dictionnaire)
	for k, v in mon_dictionnaire.items():
		print("{} : {}".format(k, " ".join(v)))

if __name__ == '__main__':
	var_to_dyc()