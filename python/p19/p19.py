#!/usr/bin/env python

#0=sunday
#0 = jan 1 1900
dow=1
c=0
dim=[31,28,31,30,31,30,31,31,30,31,30,31]
months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December"]

for y in xrange(0,101):
    if y%4 == 0:
        if (y%100==0 and (y+300)%400!=0):
            dim[1]=28
        else:
            dim[1]=29
    else:
        dim[1]=28
    for m in xrange(12):
        if dow==0:
            c+=1
        print "(",m+1,1900+y,")",dow
        dow+=dim[m]
        dow%=7

print c-2 #2 in year 1900
