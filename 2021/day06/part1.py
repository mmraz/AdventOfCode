#!/usr/bin/env python3

inputs = list()
DEBUG = False

with open('input.ex', 'r') as f:
    inputs = f.read().splitlines()
fish = [int(i) for i in inputs.pop().split(',')]
if DEBUG:
    print(f"{fish} length {len(fish)}")
day = 0

def maki(age):
    if age == 0:
        return 6
    return age-1

while(day < 256):
    babies = len([z for z in fish if z == 0])
    if DEBUG:
        print(f"babies {babies}")
    day += 1
    if DEBUG:
        print(f"day {day}")
    fish = list([maki(f) for f in fish] + [8]*babies)
    if DEBUG:
        print(f"{fish} length {len(fish)}")

print(len(fish))
