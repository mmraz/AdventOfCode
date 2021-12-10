#!/usr/bin/env python3
from collections import deque

inputs = list()
DEBUG = False

with open('input', 'r') as f:
    inputs = f.read().splitlines()

pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}

points = {')': 3, ']': 57, '}': 1197, '>': 25137}


def score_corruption(line):

    cq = deque()

    for i, c in enumerate(line):
        if c in pairs.keys():
            cq.appendleft(pairs[c])
        elif c != cq[0]:
            if DEBUG:
                print(line)
                print(f"unexpected close at {i} {c}")
            return points[c]
        elif c == cq[0]:
            cq.popleft()

    return 0


score = list()
for line in inputs:
    score.append(score_corruption(line))

print(sum(score))
