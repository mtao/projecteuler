#!/usr/bin/env python
def isPalendrome(num):
    s = str(num)
    for m in xrange(len(s)/2):
        if s[m]!=s[-m-1]:
            return False
    return True

maxPal=0
for n in xrange(100,1000):
    for m in xrange(100,1000):
        prod=n*m
        if isPalendrome(prod) and prod>maxPal:
            maxPal = prod

print maxPal
            

