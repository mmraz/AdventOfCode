#!/usr/bin/env python3

DEBUG = True

with open('input', 'r') as f:
    inputs = f.read().splitlines()

entry_mid = (len(inputs)/2)
ones = [0]*len(inputs[0])
gamma = [0]*len(inputs[0])
epsilon = [0]*len(inputs[0])

while(len(inputs) > 0):
  line = inputs.pop(0)
  ll = [int(v) for v in line]
  ziplist = zip(ll,ones)
  ones = [x + y for (x,y) in ziplist]

for x in range(len(ones)):
    if ones[x] > entry_mid:
        gamma[x] = 1
    else:
        epsilon[x] = 1

gamma_int = int(''.join([str(g) for g in gamma]),2)
epsilon_int = int(''.join([str(e) for e in epsilon]),2)
if DEBUG:
    print(f"gamma {gamma_int} epsilon {epsilon_int}")

print(gamma_int * epsilon_int)
