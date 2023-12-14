#!/usr/bin/env python3

import re

inputs = []
DEBUG = False

with open('input', 'r') as f:
    inputs = f.read().splitlines()

results = [i for i in range(1,len(inputs)+1)]

possible_limits = {'red': 12, 'green': 13, 'blue': 14}

def max_cubes(line: str, check_color: str) -> int:
    cubes = re.findall(r'(\d+) (\w+)', line)
    if DEBUG:
        print(cubes)
    return max(int(cnt) for cnt, color in cubes if color == check_color)

for gid, line in enumerate(inputs, start=1):
    for color in possible_limits.keys():
        if max_cubes(line, color) > possible_limits[color]:
            if DEBUG:
              print(f'Game {gid} fail {color}')
            results[gid-1] = 0
            break

if DEBUG:
  print(results)
print(sum(results))
