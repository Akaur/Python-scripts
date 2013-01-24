#!/usr/bin/env python
from math import *
a=-0.5
b=2
print "  Left Cardoid,1,3"
for t in range(0,360):
	x = a* (b * cos(radians(t)) - cos(radians(2*t)))
	y = a* (b * sin(radians(t)) - sin(radians(2*t)))
	print x,",",y
