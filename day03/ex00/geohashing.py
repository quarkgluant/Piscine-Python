#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import antigravity, sys

#for test :
# ./geohashing.py 37.421542 -122.085589 2005-05-26-10458.68
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("""il faut 3 arguments : 
lat: 37.421542
long: -122.085589
date sous cette forme avec l'heure-minute-seconde convertie en seconde   2005-05-26-10458.68""")
        sys.exit(0)
    
    antigravity.geohash(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3].encode())
