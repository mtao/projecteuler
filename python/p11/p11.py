#!/usr/bin/env python
split_int=lambda x: map(int, x.split())
grid=map(split_int, open("grid.txt").readlines())

m=0
#horizontal
for j in xrange(len(grid)):
    for i in xrange(len(grid[j])-4):
        m=max(reduce(lambda x,d: x*grid[i+d][j], xrange(4),1),m)
#vertical
for j in xrange(len(grid)-4):
    for i in xrange(len(grid[j])):
        m=max(reduce(lambda x,d: x*grid[i][j+d], xrange(4),1),m)
#diagonal \
for j in xrange(len(grid)-4):
    for i in xrange(len(grid[j])-4):
        m=max(reduce(lambda x,d: x*grid[i+d][j+d], xrange(4),1),m)
#diagonal /
for j in xrange(4,len(grid)):
    for i in xrange(len(grid[j])-4):
        m=max(reduce(lambda x,d: x*grid[i+d][j-d], xrange(4),1),m)

print m
