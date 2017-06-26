#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#from path import Path
import requests
#import bs4 #BeautifulSoup
import bs4 as BeautifulSoup
import sys

#use pip3 install -r requirement.txt
#https://fr.wikipedia.org/wiki/Bijou

def get_next_subject(subject):
    subject = subject.replace(' ', '%20')
    r = requests.get("https://en.wikipedia.org/wiki/" + subject)

    if r.status_code != 200:
        print("invalid response for \"%s\": code %i" % (subject, r.status_code))

    soup = BeautifulSoup.BeautifulSoup(r.content, 'html.parser')

    d = soup.find('div',attrs={'class':u'mw-parser-output'})

    for child in d.children:
        if child.name == "p":
            les_a = child.find_all('a')
            for a in les_a:
                href = str(a.get('href'))
                if href.startswith("/wiki/") \
                and not (href.startswith("#") \
                        or href.startswith("/wiki/Wikipedia:")
                        or href.startswith("/wiki/Help")):
                    return href.replace("/wiki/", "")

def roads_to_philosopy(subject):
    if subject == "Philosophy":
        print ("0 roads from Philosophy to philosophy !")
        return

    print( subject )
    tab_of_visited = [subject]

    visited = get_next_subject(subject)
    nb = 1
    while visited is not None and visited not in tab_of_visited :
        print(visited)
        tab_of_visited.append(visited)
        visited = get_next_subject(visited)

    if visited == "Philosophy":
        print ("%i roads from %s to Philosophy !", nb, subject)
        return
    else:
        print ("It's a dead end !")
        return


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("""usage: roads_to_philosopy.py [<subject>]

            Combien faut-il parcourir de wikilien, (en cliquqnt sur le premier) pour atteindre la page Philosophy.
            If no argument is given, just print this message.
    """)
        sys.exit(0)
    try:
        roads_to_philosopy(sys.argv[1])
    except Exception as e:
        print("Sorry, something's went wrong : ", e)
