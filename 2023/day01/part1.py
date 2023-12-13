#!/usr/bin/env python3

inputs = []
results = []
DEBUG = False

with open('input', 'r') as f:
    inputs = f.read().splitlines()


for line in inputs:
    digits = ''.join(filter(str.isdigit, line))
    results.append(int(f'{digits[0]}{digits[-1]}'))
  
if DEBUG:
    print(results)

print(sum(results))
