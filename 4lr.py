#!/usr/bin/env python
from math import *
R=60
r=-15
p=45
print "Four leaved Rose,1,5"
for t in range(0,90):
	x=(R+r) * cos(t) + p * cos(((R+r)*t)/r)
	y=(R+r) * sin(t) + p * sin(((R+r)*t)/r) 
	print x,",",y
