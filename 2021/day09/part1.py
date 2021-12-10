#!/usr/bin/env python3
import numpy

DEBUG = False

vents = numpy.genfromtxt('input', delimiter=1)
if DEBUG:
    print(vents)

# put a fence of 9 around the outside to prevent index out of range on edges
vents = numpy.pad(vents, pad_width=1, mode='constant', constant_values=9)
# check above, below, before and after each position for greater height
pits = ((vents < numpy.roll(vents, 1, 0)) & (vents < numpy.roll(vents, -1, 0))
        & (vents < numpy.roll(vents, 1, 1)) & (vents < numpy.roll(vents, -1, 1)))
if DEBUG:
    print(pits)

lows = numpy.extract(pits, vents)
if DEBUG:
    print(lows)
# add 1 to all the values because "risk level"
print(int((lows+1).sum()))
