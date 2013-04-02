#!/usr/bin/env python

ones=["zero","one","two","three","four","five","six","seven","eight","nine"]
tens=["zero","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
spec_tens=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
print len(ones),len(tens),len(spec_tens)

lo=map(len,ones)
lt=map(len,tens)
lst=map(len,spec_tens)
count=0
ocount=0
def numDigits(m):
    c=0
    d1=m%10
    m=m/10
    d2=m%10
    m=m/10
    d3=m%10
    print d3,d2,d1
    if d3>0:
        c+=lo[d3]+len("hundred")
        print ones[d3],"hundred",
    if d3>0 and d1+d2>0:
        print "and",
        c+=len("and")
    if d2>0:
        if d2==1:
            c+=lst[d1]
            print spec_tens[d1]
            return c
        c+=lt[d2]
        print tens[d2],
    if d1>0:
        c+=lo[d1]
        print ones[d1],
    print
    return c
for m in xrange(1,1000):
    ocount=count
    count+=numDigits(m)
    print "+",count-ocount


count+=len("onethousand")

print count
print numDigits(342)
print numDigits(115)

