#!/usr/bin/env python

        d.append(int(m))
    return d

def digit_sum(x):
    return sum(list(map(int,str(x))))

def digit_mult(a,b):
    return digit_sum(digit_sum(a)*digit_sum(b))

def digit_acc(a,b):
    return digit_sum(a*digit_sum(b))

class digit:
    def __init__(self):
        self.val=[0]
    
    def add(self,other):


    #array access
    def __setitem__(i,y):
        self.val[i]=y
    def __getitem__(i):
        return self.val[i]

acc=1
for m in range(1,1000):
    acc=digit_mult(acc,m)

print(acc)

def big_fact(n):
    if n<=1:
        return [1]
    prev = big_fact(n-1)
    return mult(prev,int2arr(n))



