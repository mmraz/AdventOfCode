#!/usr/bin/env python3
import itertools

inputs = list()
DEBUG = False

with open('input', 'r') as f:
    inputs = f.read().splitlines()

lines = [[tuple([int(x) for x in t.split(',')]) for t in pair.split(' -> ')] for pair in inputs]
if DEBUG:
    for l in lines:
        print(f"{l}")

# walk through the list from the end
# -capture the max x and y to intialize our grid
# -delete diagonal lines
x = 0
y = 0
def hline(line):
    if line[0][0] == line[1][0]:
        return True

def vline(line):
    if line[0][1] == line[1][1]:
        return True

for l in range(len(lines)-1,-1,-1):
    x = max(x, lines[l][0][0], lines[l][1][0])
    y = max(y, lines[l][0][1], lines[l][1][1])
    if not hline(lines[l]) and  not vline(lines[l]):
        if DEBUG:
            print(f"deleting {lines[l]}")
        lines.pop(l)

field = []
for l in range(y+1):
    field.insert(l,list(itertools.repeat(0, x+1)))
if DEBUG:
    for l in field:
        print(f"{l}")
    print(f"max x {x} y {y}")

def add_line(field, line):
    if hline(line):
        start = min(line[0][1],line[1][1])
        end = max(line[0][1],line[1][1])+1
        if DEBUG:
          print(f"start {start} end {end}  {line[0][0]}")
        for y in range(start,end):
            if DEBUG:
                print(f"field[{line[0][0]}][{y}] += 1")
            field[line[0][0]][y] += 1
    else:
        start = min(line[0][0],line[1][0])
        end = max(line[0][0],line[1][0])+1
        if DEBUG:
            print(f"start {start} end {end} y {line[0][1]}")
        for x in range(start,end):
            if DEBUG:
                print(f"field[{x}][{line[0][1]}] += 1")
            field[x][line[0][1]] += 1

for line in lines:
    add_line(field, line)

if DEBUG:
    for l in field:
        print(f"{l}")

avoids = 0
for l in field:
    avoids += len([x for x in l if x >= 2])

print(avoids)
