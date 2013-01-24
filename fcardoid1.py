#!/usr/bin/env python
from math import *
a=2
b=0.5
print "  Double Cardoid,1,2"
for t in range(0,360):
	x = a* (b * cos(radians(t)) - cos(radians(2*t)))
	y = a* (b * sin(radians(t)) - sin(radians(2*t)))
	print x,",",y
