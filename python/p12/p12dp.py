#!/usr/bin/env python
facts={1:{1:1}}




def factorize(n):

    if n in facts:
        return facts[n]
    facts[n]={}
    for m in xrange(2,n):
        if n%m==0:
            for o in factorize(m):
                if o in facts[n]:
                    facts[n][o]+=facts[m][o]
                else:
                    facts[n][o]=facts[m][o]
            for o in factorize(n/m):
                if o in facts[n]:
                    facts[n][o]+=facts[n/m][o]
                else:
                    facts[n][o]=facts[n/m][o]
            return facts[n]
    facts[n]={n:1}
    return facts[n]

n=0
f=0
while True:
    f=n*(n+1)/2
    '''
    if n%2==0:
        factorize(n/2)
        factorize(n+1)
    else:
        factorize(n)
        factorize((n+1)/2)
        '''
    factorize(f)
    if reduce(lambda x,y: x*(facts[f][y]+1),facts[f].keys(),1)>500:
        break
    n+=1
print facts
print n, f, reduce(lambda x,y: x*(facts[f][y]+1),facts[f],1)
