#!/usr/bin/env python3
# -*-coding:utf-8 -*

def arg_list(chaine):
    """traite les parametres fournis dans la ligne de commande"""
    liste = [item for item in chaine.split(',')]
    liste = [item.lstrip().rstrip().title() for item in liste if item != '' and item != '\t']
    # print(liste)
    return liste

def reverse_dict(dico):
    """prend un dict en argument et le retourne inversé, les clés permuttant avec les valeurs"""
    return dict([[v, k] for k, v in dico.items()])


def all_in(argv):
    """Prend une capitale ou un état en argument et renvoie l'état ou la capitale correspondant ou Unknow state"""
    import sys

    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    if len(sys.argv) != 2:
        sys.exit(1)
    liste = arg_list(sys.argv[1])

    states_rev = reverse_dict(states)
    capital_cities_rev = reverse_dict(capital_cities)

    for item in liste:
        if item in states:
            print("{0} is the capital of {1} (akr: {2})".format(capital_cities[states[item]], item, states[item]))
        elif item in capital_cities_rev:
            print("{0} is the capital of {1} (akr: {2})".format(item, states_rev[capital_cities_rev[item]], capital_cities_rev[item]))
        else:
            print("{0} is neither a capital city nor a state".format(item))



if __name__ == '__main__':
    import sys
    all_in(sys.argv)
    