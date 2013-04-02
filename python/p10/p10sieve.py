#!/usr/bin/env python
r=range(2,2000000)
for n in xrange(len(r)):
    v=r[n]
    if v==0:
        continue
    c=n+v
    while c<len(r):
        r[c]=0
        c+=v
print sum(r)
