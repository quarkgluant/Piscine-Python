#!/usr/bin/env python3
# -*-coding:utf-8 -*-
from settings import *

#
# def lecture():
#     import sys
#     print(globals())
#     try:
#         with open("settings.py", "r") as mon_fichier:
#             contenu = mon_fichier.read()
#             contenu = contenu.replace(' = ', '=').replace('\n', ',')
#             # mon_dico = dict((k,v) for k,v in (item.split('=') for item in contenu.split(',')))
#             ma_list = (item.split('=') for item in contenu.split(','))
#             mon_dico = dict((elem[0], elem[1].replace('"', '')) for elem in ma_list)
#             # print(mon_dico)
#
#             return mon_dico
#
#     except FileNotFoundError as e:
#         print('le fichier {} n\'existe pas.'.format(e.filename))
#         sys.exit(1)
#     except PermissionError as e:
#         print('Droits de lecture absent sur le fichier{}'.format(e.filename))
#         sys.exit(2)
#     except Exception as e:
#         print('Une erreur a empeché l\'ouverture du fichier.'.format(e.strerror))
#         sys.exit(3)

def ecriture():
    """prend un fichier .template et remplace dans celui-ci les valeurs entre {} par celles indiquées dans le fichier settings.py"""
    import sys, re
    if len(sys.argv) != 2:
        print("usage: render.py <file>.template ")
        sys.exit(0)

    filename = sys.argv[1]
    try:
        # for filename in os.listdir(os.getcwd()):
        #     # print(os.getcwd())
        #     # print(filename)
        #     if re.match("\w+.template", filename):
                # print(filename)
        if re.match("\w+.template", filename):
            with open(filename, 'r') as f:
                contenu = f.read()
                # print(globals())
                a_ecrire = contenu.format_map(globals())
                # print(a_ecrire)
                # print(filename)
                file_html = filename.replace('.template', '.html')
                # print(file_html)
            with open(file_html, 'w') as f_h:
                f_h.write(a_ecrire)
        else:
            print("le fichier {} n'a pas .template comme extension.".format(filename))
            sys.exit(0)
    except FileNotFoundError as e:
        print("le fichier {} n'existe pas.".format(e.filename))
        sys.exit(0)
    except PermissionError as e:
        print("Droits de lecture absent sur le fichier{}".format(e.filename))
        sys.exit(0)
    except Exception as e:
        print("Une erreur a empeché l'ouverture du fichier.".format(e))
        sys.exit(0)

if __name__ == '__main__':
    ecriture()