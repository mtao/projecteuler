#!/usr/bin/env python
digits=[1]

m2=[0,2,4,6,8,0,2,4,6,8]

def p2():
    carry=0
    for m in xrange(len(digits)):
        digits[m],carry=m2[digits[m]] + carry,digits[m]/5
    if carry>0:
        digits.append(carry)




for x in xrange(1000):
    p2()
    print x+1, digits

print digits
print sum(digits)


