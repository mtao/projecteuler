#!/usr/bin/env python3
from math import log
a = (1+5**.5)/2
b = (1-5**.5)/2

def fib(n):
    return (a**n-b**n)/(a-b)


fp = 1
fc = 1
fci = 2

#while log(fc,10) < 3:
while log(fc,10)+1 < 1000:
    fc,fp = fc+fp,fc
    fci += 1
#    print("{0}: {1}, {2}".format(fci,fc,len(str(fc))))
print("{0}: {1}, {2}".format(fci,fc,len(str(fc))))

