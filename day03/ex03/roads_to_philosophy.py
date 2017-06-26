#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, requests
from bs4 import BeautifulSoup

def filter(tag):
	from bs4 import BeautifulSoup

	return tag is not None  and not tag.has_attr("role") and not tag.name == "abbr" and not tag.name == "img" and tag.name == 'a'



def wikipedieur(mot):
	import sys, requests
	from bs4 import BeautifulSoup


	req = requests.get("https://en.wikipedia.org/wiki/{}".format(mot))

	if req.status_code != 200 or not req:
		print("Argh grosse Problem sur le serveur")
		sys.exit(0)

	if not req.text:
		print("c'est quoi ce mot {} qui n'existe pas?".format(mot))
		sys.exit(0)


	soup = BeautifulSoup(req.text, 'html.parser')
	# print(soup.prettify())
	# //div[@id='mw-content-text']//p/a[starts-with(@href, '/wiki/')]

	et_de_un = soup.find('div',attrs={"id":u"bodyContent"}).find('div',attrs={"id":u"mw-content-text"}).find('div',attrs={"class":u"mw-parser-output"})
	for child in et_de_un.children:
		if child.name == "p":
			les_a = child.find_all(filter)
			for a in les_a:
				href = str(a.get('href'))
				if href.startswith("/wiki/") \
				and not (href.startswith("#") \
						or href.startswith("/Wikipedia:")
						or href.startswith("/wiki/Help")
						or href.startswith('/wiki/File')
						or href.startswith('/wiki/Wikipedia:Citation_needed')
						or href.startswith('//upload.wikimedia.org/')):
					# print("href " + href.replace("/wiki/", ""))
					return href.replace("/wiki/", "")


def wikipedions():
	import sys
	if len(sys.argv) != 2:
		print("""il faut 1 argument : 
un nom à rechercher sur wikipedia""")
		sys.exit(0)

	mot = sys.argv[1]
	

	if mot == "Philosophy":
		print ("0 roads from Philosophy to philosophy !")
		sys.exit(0)

	print( mot )
	tab_philo = [mot]

	visited = wikipedieur(mot)
	while visited is not None :
		mot.replace(' ', '_')
		print(visited)
		tab_philo.append(visited)
		visited = wikipedieur(visited)

		if visited == "Philosophy":
			iteration = len(tab_philo)
			print ("{} roads from {} to Philosophy !".format(iteration, mot))
			sys.exit(0)
		elif visited  in tab_philo:
			print("It leads to an infinite loop ! ")
			sys.exit()


if __name__ == '__main__':

	wikipedions()
	