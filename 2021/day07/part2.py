#!/usr/bin/env python3

inputs = list()
DEBUG = False

with open('input', 'r') as f:
    inputs = f.read().splitlines()
crabs = [int(i) for i in inputs.pop().split(',')]
if DEBUG:
    print(f"{crabs} length {len(crabs)}")

end = max(crabs)+1
fuel = int(end*(end+1)/2)*len(crabs)
if DEBUG:
    print(f"fuel {fuel}")

for tpos in range(end):
  fuel_cost = sum([int(abs(f-tpos)*(abs(f-tpos)+1)/2) for f in crabs])
  if DEBUG:
    print(f"to position {tpos} fuel cost {fuel_cost}")
  if fuel_cost < fuel and DEBUG:
    print(f"lower fuel {fuel_cost}")
  fuel = min(fuel, fuel_cost)

print(fuel)
  
