#!/usr/bin/env python3

DEBUG = False

with open('input', 'r') as f:
    inputs = f.read().splitlines()

position = 0
depth = 0

while(len(inputs) > 0):
  line = inputs.pop(0)
  if( line.startswith('f') ):
      position += int(line.rsplit(' ',1)[-1])
  if( line.startswith('d') ):
      depth += int(line.rsplit(' ',1)[-1])
  if( line.startswith('u') ):
      depth -= int(line.rsplit(' ',1)[-1])

if DEBUG:
  print(inputs)
print(position * depth)
