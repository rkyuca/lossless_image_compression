'''
Reference:  https://en.wikipedia.org/wiki/Hilbert_curve . 
Hilber space filling curve on nxn 2d space with n being power of 2. 
(x,y) coordinates (0,0) at bottom left and (n-1,n-1) in top right.
d is 0 at lower left and n^2 -1 on lower right. 
---@RK, 26th October, 2018
'''


import numpy as np


def xy2d ( n,  x, y) :
    d=0
    s=int(n//2)
    while s>0:
        #import ipdb;ipdb.set_trace()
        rx=int( ( x & s)>0)
        ry= int((y& s)> 0)
        d+=s*s*((3*rx)^ry)
        x,y=rot(s,x,y,rx,ry)
        s=s//2   
    return d



def d2xy( n, d):
    s=1
    t=d
    x=0
    y=0
    while s<n:
        rx=1& (t/2)
        ry=1& (t^rx)
        x,y=rot(s, x, y, rx, ry)
        x=x+s*rx
        y=y+s*ry
        t=t/4
        s*=2
    return x, y


#rotate/flip a quadrant appropriately
def rot( n, x, y,  rx, ry):
    if ry == 0: 
        if rx == 1: 
            x = n-1 - x;
            y = n-1 - y;
        #Swap x and y
        t  = x;
        x = y;
        y = t;
    return x, y    
   
