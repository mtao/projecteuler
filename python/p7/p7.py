#!/usr/bin/env python
p=[]
n=2
while len(p)<10001:
    isPrime=True
    for pr in p:
        if n%pr==0:
            isPrime=False

    if isPrime:
        p.append(n)
    n+=1

print p[-1]

