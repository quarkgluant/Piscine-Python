#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def wikipedieur():
	import sys, requests, json
	from dewiki import parser
	if len(sys.argv) != 2:
		print("""il faut 1 argument : 
un nom à rechercher sur wikipedia""")
		sys.exit(0)

	mot = sys.argv[1]

	req = requests.get("https://fr.wikipedia.org/w/api.php?action=query&titles={}&prop=revisions&rvprop=content&format=json".format(mot))

	if req.status_code != 200 or not req:
		print("Argh grosse Problem sur le serveur")
		sys.exit(0)

	if not req.text:
		print("c'est quoi ce mot {} qui n'existe pas?".format(mot))
		sys.exit(0)

	on_avance = json.loads(req.text)
	le_graal = on_avance['query']['pages']

	# print(le_graal)
	for k in le_graal.keys():
		for k2 in le_graal[k].keys():
			if k2 == "revisions":
				tresor =  le_graal[k][k2]
				break


	mon_parser = parser.Parser()
	try:
		good = tresor[0]['*']
		to_write = mon_parser.parse_string(good)
		# print(mon_parser.parse_string(good))
		wiki_file = "{}.wiki".format(sys.argv[1])
		with open(wiki_file, 'w') as f:
			f.write(to_write)
	except:
		print("inconnu au bataillon")
		sys.exit(0)

if __name__ == '__main__':
	wikipedieur()
