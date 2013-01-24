#!/usr/bin/env python
from math import *
R=12
r=2
print " Epicycloid,1,5"
for s in range(0,360):
	x = (R + r) * cos(radians(s)) + r * cos(radians((R/r + 1)*s))
	y = (R + r) * sin(radians(s)) - r * sin(radians((R/r + 1)*s))
	print x,",",y
