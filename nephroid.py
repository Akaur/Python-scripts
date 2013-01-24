#!/usr/bin/env python
from math import *
R=1
r=0.5
print "Nephroid,1,4"
for t in range(0,60):
	x=(R+r) * cos(t) + r * cos(((R+r)/r)*t)
	y=(R+r) * sin(t) + r * sin(((R+r)/r)*t) 
	print x,",",y
