#!/usr/bin/env python3
# -*-coding:utf-8 -*

import sys
import requests
import bs4 as BeautifulSoup


def search_word(word):
   listeword = []


   while (1):


       if word == 'Philosophy':
           listeword.append(word)
           for c in listeword:
               print (c)
           print("{} roads from {} to {} !".format(len(listeword), listeword[0], listeword[-1]))
           return

       if word in listeword:
           print('It leads to an infinite loop !')
           return
       else:
           listeword.append(word)

       url = "https://en.wikipedia.org/wiki/" + word
       r = requests.get(url)

       if r.status_code != 200:
           if r.status_code == 404:
               print("Nothing was found for {}".format(word))
               return
           else:
               print("Erreur lors de la récupération de l'adresse code {}".format(r.status_code))
               return
       # print(r.text)

       listeword.append(word)
       soup = BeautifulSoup.BeautifulSoup(r.text, "html.parser")
       title = str(soup.find("title")).split('-', 1)[0].split('>', 1)[1].strip()


       s = soup.find('div', attrs={"id": u"bodyContent"}).find('div', attrs={"id": u"mw-content-text"}).find('div', attrs={"class": u"mw-parser-output"})
       if not s:
           print('It leads to a dead end !')
           return
       p = []
       for child in s.children:
           if child.name == 'p':
               p.append(child)

       if len(p) == 0:
           print('It leads to a dead end !')
           return
       a_all = []
       for child in p:
           for child1 in child:
               if child1.name == 'a':
                   a_all.append(child1)


       if len(a_all) == 0:
           print('It leads to a dead end !')
           return
       z = []
       for c in a_all:
               try:
                   title=c["title"]
               except:
                   title=None
               if not title:
                   continue
               if not (title.startswith('Help:')) and (not title.startswith('Wikipedia:Citation needed')):
                   try:
                       z.append(c["href"])
                   except:
                       continue
       if len(z) == 0:
           print('It leads to a dead end !')
           return
       word = z[0].split('/')[2]


   # for a in listeword:
   #     print (a)


if __name__ == '__main__':

   if len(sys.argv) != 2:
       print('You must enter one name to start the search')
       quit()
   search_word(sys.argv[1])