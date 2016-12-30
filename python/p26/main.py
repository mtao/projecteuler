#!/usr/bin/env python3
from math import floor


def repeatNum(num):
    r = 1
    rhist = set()
    while r != 0 :
        r *= 10
        v = floor(r/num)
        r = r % num
        if r in rhist:
            return len(rhist)
        else:
            rhist.add(r)
    return len(rhist)



mv = 0
for m in range(2,1000):
    v = repeatNum(m)
    mv = max(v,mv)

print(mv+1)#need to figure out what to deal with this extra one?

