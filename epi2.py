#!/usr/bin/env python
from math import *
R=12
r=3
c=5
print " Epitrochoid,1,4"
for s in range(0,360):
	x = (R + r) * cos(radians(s)) + c * cos(radians((R/r + 1)*s))
	y = (R + r) * sin(radians(s)) - c * sin(radians((R/r + 1)*s))
	print x,",",y
