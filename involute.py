#!/usr/bin/env python
from math import *
a=0.1
print " Involute of a Circle ,1,1"
for t in range(0,1440):
	x = a*(cos(radians(t)) + t*sin(radians(t)))
	y = a*(sin(radians(t)) - t*cos(radians(t)))
	print x,",",y


