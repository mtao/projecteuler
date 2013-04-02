#!/usr/bin/env python

chain={1:1}

maxn=0
max=0
for n in xrange(1,1000000):
    if n not in chain:
        t=n
        ops=[]
        while t not in chain:
            if t%2==0:
                ops.append(0)
                t=t/2
            else:
                ops.append(1)
                t=3*t+1
        while len(ops)>0:
            op=ops.pop()
            if op==0:
                chain[t*2]=chain[t]+1
                t=t*2
            if op==1:
                chain[(t-1)/3]=chain[t]+1
                t=(t-1)/3
    if chain[n]>max:
        max=chain[n]
        maxn=n
print chain
print maxn, max
    
