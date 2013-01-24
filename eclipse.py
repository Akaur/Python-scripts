#!/usr/bin/env python
from math import *
R=60
r=-30
p=-90
print "ecllipse,1,3"
for t in range(0,60):
	x=(R+r) * cos(t) + p * cos(((R+r)*t)/r)
	y=(R+r) * sin(t) + p * sin(((R+r)*t)/r) 
	print x,",",y
