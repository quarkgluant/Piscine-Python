#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from path import Path

if __name__ == '__main__':
	tmp = Path('.')
	tmp = tmp / 'dossier'
	if not tmp.isdir():
		tmp.mkdir()
	nouv = tmp / 'fichier.txt'
	if not nouv.isfile():
		nouv.touch()
	nouv.write_text("Et path dans ta tronche!")
	for line in nouv.lines():
		print (line)
