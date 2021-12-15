#!/usr/bin/env python3
import numpy as np

DEBUG = False

with open('input', 'r') as f:
    inputs = f.read().splitlines()
    folds = [tuple(f.split()[2].split('=')) for f in inputs if 'f' in f]
    if DEBUG:
        print(folds)

points = np.genfromtxt('input', converters={0: lambda x: int(x), 1: lambda y: int(y)}, delimiter=',', comments='fold')
if DEBUG:
    print(points)
max_x = max([x for (x, y) in points])+1
max_y = max([y for (x, y) in points])+1
if DEBUG:
    print(f"max_x {max_x} max_y {max_y}")
paper = np.zeros(shape=(max_y, max_x), dtype=bool)
for (x, y) in points:
    paper[y][x] = True
if DEBUG:
    print(paper)


def foldit(paper, folds):
    for axis, fold in folds:
        fold = int(fold)
        if DEBUG:
            print(f"axis {axis} fold {fold}")
        if axis == 'x':
            left = paper[:, :fold]
            right = paper[:, 2*fold:fold:-1]
            paper = left | right
        elif axis == 'y':
            top = paper[:fold]
            bottom = paper[2*fold:fold:-1, :]
            paper = top | bottom
        if DEBUG:
            print(paper)
    return(paper)


paper = foldit(paper, folds)
letters = np.full_like(paper, fill_value='.', dtype=np.str_)
letters[paper] = 'X'
a = np.hsplit(letters, 8)
for b in a:
    print(f"{b}\n")
