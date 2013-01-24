#!/usr/bin/env python
from math import *
a=2.9
b=5
c=2.7
print " Tablot's Curve ,1,1"
for t in range(0,360):
	x = ((a**2 + c*c*sin(radians(t))**2)*cos(radians(t)))/a
	y = ((a**2 - 2.0*c**2 + c*c*sin(radians(t))**2)*sin(radians(t)))/b
	print x,",",y




