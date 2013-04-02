#!/usr/bin/env python

grid=map(lambda x: map(int,x.split()),open("data.txt").readlines())
solve=map(lambda x: map(lambda x: 0, x), grid)
for m in xrange(len(grid[-1])):
    solve[-1][m]=max(grid[-1][m],0)

for m in xrange(len(grid)-2,-1,-1):
    for n in xrange(len(grid[m])):
        print grid[m][n], solve[m+1][n]
        solve[m][n]=grid[m][n]+max(solve[m+1][n],solve[m+1][n+1])
        
print solve[0]
