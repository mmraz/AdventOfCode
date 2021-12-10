#!/usr/bin/env python3
import numpy
from scipy.ndimage import label

DEBUG = False

vents = numpy.genfromtxt('input', delimiter=1)
if DEBUG:
    print(vents)

# put a fence of 9 around the outside to prevent index out of range on edges
vents = numpy.pad(vents, pad_width=1, mode='constant', constant_values=9)

basins = {}
basins['labels'], basins['counts'] = label(vents != 9)
basins['areas'] = numpy.bincount(basins['labels'][basins['labels'] != 0])
if DEBUG:
    print(basins)
print(numpy.product(numpy.sort(basins['areas'])[-3:]))
