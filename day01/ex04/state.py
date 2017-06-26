#!/usr/bin/env python3
# -*-coding:utf-8 -*

def reverse_dict(dico):
    """prend un dict en argument et le retourne inversé, les clés permuttant avec les valeurs"""
    return dict([[v, k] for k, v in dico.items()])


def state(argv):
    """Prend une capitale en argument et renvoie l'état correspondant ou Unknow state"""
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

    states_rev = reverse_dict(states)
    capital_cities_rev = reverse_dict(capital_cities)
    city = sys.argv[1]
    reponse = states_rev[capital_cities_rev[city]] if city in capital_cities_rev else "Unknow capital city"
    print(reponse)


if __name__ == '__main__':
    import sys
    state(sys.argv)
