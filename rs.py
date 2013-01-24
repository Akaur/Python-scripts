#!/usr/bin/env python
from math import *
R=60
r=-45
p=-101
print "Rounded Square,1,5"
for t in range(0,270):
	x=(R+r) * cos(t) + p * cos(((R+r)*t)/r)
	y=(R+r) * sin(t) + p * sin(((R+r)*t)/r) 
	print x,",",y
