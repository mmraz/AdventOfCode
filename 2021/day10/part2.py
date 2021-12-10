#!/usr/bin/env python3
from collections import deque
from statistics import median

inputs = list()
DEBUG = False

with open('input', 'r') as f:
    inputs = f.read().splitlines()

pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}

points = {')': 1, ']': 2, '}': 3, '>': 4}


def score_corruption(line):

    cq = deque()
    score = 0

    for i, c in enumerate(line):
        if c in pairs.keys():
            cq.appendleft(pairs[c])
        elif c != cq[0]:
            return score
        elif c == cq[0]:
            cq.popleft()

    unclosed = ''
    for c in cq:
        score *= 5
        score += points[c]
        if DEBUG:
            unclosed += c

    if DEBUG:
        print(f"inclomplete {unclosed} {score}")
    return score


scores = list()
for line in inputs:
    line_score = score_corruption(line)
    if line_score > 0:
        scores.append(line_score)

print(median(scores))
