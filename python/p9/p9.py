#!/usr/bin/env python

for c in xrange(1,1000):
    for b in xrange(1,c):
        a=1000-b-c
        if a>0 and a<b and a**2+b**2==c**2:
                print a,b,c, a*b*c
