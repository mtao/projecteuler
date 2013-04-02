#!/usr/bin/env python
p=[]
for n in xrange(2,2000000):

    isPrime=True
    for pr in p:
        if n<pr**2:
            break
        if n%pr==0:
            isPrime=False
            break;

    if isPrime:
        p.append(n)

print sum(p)
