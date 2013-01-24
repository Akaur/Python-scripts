#!/usr/bin/env python
from math import *
R=60
r=-15
p=-15
print "Astroid- A Type of Hypocycloid,1,4"
for t in range(0,180):
	x=(R+r) * cos(t) + p * cos(((R+r)*t)/r)
	y=(R+r) * sin(t) + p * sin(((R+r)*t)/r) 
	print x,",",y
