#!/usr/bin/env python

grid=[[-1 for y in xrange(21)] for x in range(21)]

def pp():
    for m in xrange(len(grid)):
        for n in xrange(len(grid)):
            print grid[m][n],
        print
grid[0][0]=1
def paths(i,j):
    if grid[i][j]==-1:
        grid[i][j]=0
        if i>0:
            grid[i][j]+=paths(i-1,j)
        if j>0:
            grid[i][j]+=paths(i,j-1)
        return grid[i][j]
    else:
        return grid[i][j]

print paths(20,20)
pp()
