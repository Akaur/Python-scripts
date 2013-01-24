#!/usr/bin/env python
from math import *
R=1
r=0.714
print "Rounded shape,1,1"
for t in range(0,60):
	x=(R+r) * cos(t) + r * cos(((R+r)/r)*t)
	y=(R+r) * sin(t) + r * sin(((R+r)/r)*t) 
	print x,",",y
