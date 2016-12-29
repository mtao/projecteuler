#!/usr/bin/end python3
from math import factorial


chars = list(range(10))
#chars = list(range(4))
numPerms = [factorial(x) for x in range(len(chars)+1)]
numPerms[0] = 0

def getPerm(permNum,l):
    remPerms = permNum;
    permsPerLoop = numPerms[len(l)-1]
    for i,v in enumerate(l):
        rsize = len(l) - i-1
        rperms = remPerms - permsPerLoop
        if rperms < 0:
            return (v,) + getPerm(remPerms,l[:i]+l[i+1:])
        else:
            remPerms = rperms
    return (l[0],)



print("".join(map(str,getPerm(10**6-1,chars))))

