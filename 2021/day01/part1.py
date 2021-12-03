#!/usr/bin/env python3

DEBUG = False

with open('input', 'r') as f:
    inputs = list(map(int,f.read().splitlines()))

increase_cnt = 0
a = inputs.pop(0)

while(len(inputs) > 0):
  if a < inputs[0]:
      increase_cnt += 1
  a = inputs.pop(0)

if DEBUG:
  print(inputs)
print(increase_cnt)
