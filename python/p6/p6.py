#!/usr/bin/env python

n=100
ssq=((n*(n+1))/2)**2
sqs=reduce(lambda x,y:x+y**2, xrange(n+1))
print ssq-sqs
