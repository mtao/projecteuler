#!/usr/bin/env python

primes=[2,[2]]
amicable={}

def gen_primes(n):
    if primes[0]>n:
        return
    for m in range(primes[1][-1],n+1):
        isPrime(m)
    primes[0]=n

def isPrime(n):
    for m in primes[1]:
        if n%m==0:
            return
    primes[1].append(n)

def factor(n):
    gen_primes(n)
    f={}
    while n>1:
        for p in primes[1]:
            if n%p==0:
                n=n/p
                if p in f:
                    f[p]+=1
                else:
                    f[p]=1

    return f

def d(n):
    if n in amicable:
        return amicable[n]
    fn=factor(n)
    r=1
    for k in fn:
        tmp=0
        for m in range(fn[k]+1):
            tmp+=k**m
        r*=tmp
    r=r-n
    amicable[n]=r
    return r

print(220,d(220),d(d(220)))

sum=0
for m in range(2,10000):
    #print(m)
    #print(a,b,c)
    if m==d(d(m)) and m!=d(m):
        sum+=m
        print(m,d(m))
    

print(sum)
