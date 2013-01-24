#!/usr/bin/env python
from math import *
R=75
r=-25
p=85
print "Gold Fish,1,2"
for t in range(0,180):
	x=(R+r) * cos(t) + p * cos(((R+r)*t)/r)
	y=(R+r) * sin(t) + p * sin(((R+r)*t)/r) 
	print x,",",y
