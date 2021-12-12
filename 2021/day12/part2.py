#!/usr/bin/env python3
from collections import defaultdict

DEBUG = False

with open('input', 'r') as f:
    inputs = [line.split('-') for line in f.read().splitlines()]
    if DEBUG:
        print(inputs)

tunnels = defaultdict(set)
for f, t in inputs:
    tunnels[f].add(t)
    tunnels[t].add(f)
if DEBUG:
    print(tunnels)


def spelunk(path, deeper):
    if DEBUG:
        print(f"in path {path}")
    if path[-1] == 'end':
        return 1

    paths = 0
    for t in tunnels[path[-1]]:
        if DEBUG:
            print(f"path {path}\nt {t}")
        if not (t.islower() and t in path):
            paths += spelunk(path + (t, ), deeper)
        elif deeper and path.count(t) == 1 and t != 'start':
            paths += spelunk(path + (t, ), False)
    return paths


print(spelunk(('start', ), True))
