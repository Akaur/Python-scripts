#!/usr/bin/env python
from math import *
R=12
r=3
c=5
print "Four leaved Rose,1,5"
for t in range(0,360):
	x=((R-r) * cos(radians(t)))+(c * cos(radians((R/r-1)*t)))
	y=((R-r) * sin(radians(t)))-(c * sin(radians((R/r-1)*t)))
	print x,",",y
