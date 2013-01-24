#!/usr/bin/env python
from math import *
a=1
print " Nephroid ,1,3"
for t in range(0,360):
	x = a*(3.0*cos(radians(t)) - cos(radians(3.0*t)))
	y = a*(3.0*sin(radians(t)) - sin(radians(3.0*t)))
	print x,",",y


