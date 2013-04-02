#!/usr/bin/env python

n=1
while True:
    t=n*(n+1)/2
    f=1
    for m in xrange(1,t):
        if t%m==0:
            f+=1
    if n%100==0:
        print n, t, f
    if f>500:
        break
    n+=1

print n, n*(n+1)/2
