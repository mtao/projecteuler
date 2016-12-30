#!/usr/bin/env python3


edge_width = 1001


dim = int((edge_width+1)/2)


s=1
for r in range(1,dim):
    inc = 2*r
    pv = (2*r-1)**2
    s+=pv * 4 + 10*inc




print(s)
