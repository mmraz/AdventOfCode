#!/usr/bin/env python3

import re

inputs = []
DEBUG = False

with open('input', 'r') as f:
    inputs = f.read().splitlines()

results = []


def max_cubes(line: str, check_color: str) -> int:
    cubes = re.findall(r'(\d+) (\w+)', line)
    if DEBUG:
        print(cubes)
    return max(int(cnt) for cnt, color in cubes if color == check_color)


for line in inputs:
  power = max_cubes(line, 'red')
  power = power * max_cubes(line, 'green')
  power = power * max_cubes(line, 'blue')

  results.append(power)

if DEBUG:
  print(results)
print(sum(results))
