#!/usr/bin/env python

primes=[]
def isPrime(n):
    for m in xrange(2,n):
        if n%m==0:
            return False
    primes.append(n)
    return True

def greatestPrimeFactor(n):
    print "Checking", n
    if isPrime(n):
        return n
    for m in xrange(2,n):
        if n%m==0:
            return max(greatestPrimeFactor(m), greatestPrimeFactor(n/m))

#print greatestPrimeFactor(5142)
print greatestPrimeFactor(600851475143)
