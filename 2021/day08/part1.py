#!/usr/bin/env python3
import statistics as s

inputs = list()
DEBUG = True

with open('input', 'r') as f:
    inputs = f.read().splitlines()

out_digits = list()

for line in inputs:
    if DEBUG:
        print(line.split('|'))
    out_digits.append([d for d in line.split('|').pop().split() if (len(d) in [2,3,4,7]) ])

if DEBUG:
    print(f"{out_digits} length {len(out_digits)}")

count_digits = 0
for dig in out_digits:
    count_digits += len(dig)

print(count_digits)
  
