#!/usr/bin/env python

sum=0
for n in xrange(1000):
    if n%5 == 0 or n%3 == 0:
        sum=sum+n
        print sum
print sum
