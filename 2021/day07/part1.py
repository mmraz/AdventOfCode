#!/usr/bin/env python3
import statistics as s

inputs = list()
DEBUG = False

with open('input', 'r') as f:
    inputs = f.read().splitlines()
crabs = [int(i) for i in inputs.pop().split(',')]
if DEBUG:
    print(f"{crabs} length {len(crabs)}")

mean = s.mean(crabs)
median = int(s.median(crabs))
mode = s.mode(crabs)
if DEBUG:
  print(f"mean {mean} median {median} mode {mode}")

fuel = sum(crabs)
start = min(median,mode)
end = max(median,mode)+1
for tpos in range(start,end):
  fuel_cost = sum([abs(f-tpos) for f in crabs])
  if DEBUG:
    print(f"to position {tpos} fuel cost {fuel_cost}")
  fuel = min(fuel, fuel_cost)
  if DEBUG:
    print(f"lower fuel {fuel_cost}")

print(fuel)
  
