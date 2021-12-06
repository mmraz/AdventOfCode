#!/usr/bin/env python3
import copy

inputs = list()
DEBUG = False

with open('input', 'r') as f:
    inputs = f.read().splitlines()
fish = [int(i) for i in inputs.pop().split(',')]
if DEBUG:
    print(f"{fish} length {len(fish)}")
day = 0

fishes = {x: 0 for x in range(9)}
if DEBUG:
    print(f"{fishes} length {len(fishes)}")

for age in range(9):
    fishes[age] = len([z for z in fish if z == age])
    if DEBUG:
        print(f"{fishes} length {len(fishes)}")

while(day < 256):
    day += 1
    if DEBUG:
        print(f"day {day}")
    school = dict()
    school = {0: fishes[1], 1: fishes[2], 2: fishes[3], 3: fishes[4],
              4: fishes[5], 5: fishes[6], 6: fishes[7] + fishes[0],
              7: fishes[8], 8: fishes[0]}
    if DEBUG:
        print(f"school {school}")
    fishes = copy.deepcopy(school)

print(sum([x for x in fishes.values()]))
