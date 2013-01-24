#!/usr/bin/env python
from math import *
a=1.5
print " Tricuspoid ,1,4"
for t in range(0,360):
	x = a*(2.0*cos(radians(t)) + cos(radians(2.0*t)))
	y = a*(2.0*sin(radians(t)) - sin(radians(2.0*t)))
	print x,",",y




