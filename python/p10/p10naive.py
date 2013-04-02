#!/usr/bin/env python
p=[]
#for n in xrange(2,2*1000*1000):
for n in xrange(2,2*1000*1000):
    isPrime=True
    for m in xrange(2,int(n**.5)+1):
        if n%m==0:
            isPrime=False
            break

    if isPrime:
        p.append(n)

print sum(p)
