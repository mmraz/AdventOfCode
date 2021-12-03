#!/usr/bin/env python3

DEBUG = False

with open('input', 'r') as f:
    inputs = f.read().splitlines()

position = 0
depth = 0
aim = 0

while(len(inputs) > 0):
  line = inputs.pop(0)
  if( line.startswith('f') ):
      val = int(line.rsplit(' ',1)[-1])
      position += val
      depth += (val * aim)
  if( line.startswith('d') ):
      aim += int(line.rsplit(' ',1)[-1])
  if( line.startswith('u') ):
      aim -= int(line.rsplit(' ',1)[-1])

if DEBUG:
  print(f"pos {position} dep {depth}" )
print(position * depth)
