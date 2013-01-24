#!/usr/bin/env python
from math import *
R=90
r=1
p=105
print "Rotating triangle,1,1"
for t in range(0,180):
	x=(R+r) * cos(t) + p * cos(((R+r)*t)/r)
	y=(R+r) * sin(t) + p * sin(((R+r)*t)/r) 
	print x,",",y
