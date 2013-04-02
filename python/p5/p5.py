#!/usr/bin/env python
p={}
div=range(2,21)
for n in div:
    isPrime=True
    for pr in p:
        if n%pr==0:
            isPrime=False

    if isPrime:
        p[n]=1
    else:
        print n
        for m in p:
            gp=m**p[m]
            if n%gp==0 and (n/gp)%m==0:
                p[m]+=1

prod=1
for m in p:
    prod*=m**p[m]


print p
print prod
