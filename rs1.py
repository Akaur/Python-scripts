#!/usr/bin/env python
from math import *
a=8
b=2
p=1
print "  Rounded square ,1,1"
for t in range(0,360):
	x = (a - b)*cos(radians(t)) + p*cos(radians((a/b - 1.0)*t))
	y = (a - b)*sin(radians(t)) - p*sin(radians((a/b - 1.0)*t))
	print x,",",y
