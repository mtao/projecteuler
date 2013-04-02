#!/usr/bin/env python

prev=1
cur=1
sum=0
while cur<4000000:

    if cur%2==0:
        sum += cur
    cur,prev=cur+prev,cur

print sum
