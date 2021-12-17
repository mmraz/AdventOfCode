#!/usr/bin/env python3
import re
import math
from itertools import count

DEBUG = False

with open('input') as f:
    _, ranges = f.read().strip().split(':')
    ranges = re.sub(r" [xy]=", '', ranges)
    data = ranges.replace('..', ',').split(',')
    if DEBUG:
        print(data)

xrange = range(int(data[0]), int(data[1]) + 1)
yrange = range(int(data[2]), int(data[3]) + 1)


def get_position(vx, vy, time):
    return tuple([(vx - max(0, vx-time)) * (1 + vx + max(0, vx-time))/2, -time * (time - 2 * vy - 1) / 2])


# maximum y value of the trajectory if it hits the target defaulting to  negative infinity
def max_y(vx, vy, xrange, yrange):
    maxy = min(yrange)
    for time in count():
        pos = get_position(vx, vy, time)
        maxy = max(pos[1], maxy)
        if pos[0] >= min(xrange) and pos[0] <= max(xrange) and pos[1] >= min(yrange) and pos[1] <= max(yrange):
            return maxy
        if (pos[0] >= max(xrange) or pos[1] < min(yrange)):
            return -math.inf


# minimum value of x velocity to prevent the rocket dropping vertically before it reaches the target
min_vx = int((1 + math.sqrt(1 + 8 * min(xrange)))/2)

hits = 0
for vx in range(min_vx, max(xrange)+1):
    for vy in range(min(yrange), -min(yrange)):
        z = max_y(vx, vy, xrange, yrange)
        if z > -math.inf:
            hits += 1

print(hits)
