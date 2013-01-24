#!/usr/bin/env python
from math import *
R=60
r=60
p=60
print "Cardoid,1,1"
for t in range(0,90):
	x=(R+r) * cos(t) + p * cos(((R+r)*t)/r)
	y=(R+r) * sin(t) + p * sin(((R+r)*t)/r) 
	print x,",",y
