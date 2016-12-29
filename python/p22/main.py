#!/usr/bin/end python3
lines = open("p022_names.txt").readlines()
names = lines[0].split(',')
names = [x[1:-1] for x in names]

names.sort()

def getNum(name):
    return sum(ord(x)-64 for x in name)


print("COLIN:",names.index("COLIN"))


print(sum((i+1)*getNum(v) for i,v in enumerate(names)))
