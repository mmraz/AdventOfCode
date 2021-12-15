#!/usr/bin/env python3
from functools import cache
from collections import Counter

DEBUG = False

pairs, _, *rules = open('input', 'r').read().splitlines()
rules = dict(r.split(' -> ') for r in rules)
if DEBUG:
    print(f"pairs {pairs}\nrules {rules}")


@cache
def polymerize(a, b, depth=10):
    if depth == 0:
        return Counter('')
    x = rules[a+b]
    return Counter(x) + polymerize(a, x, depth-1) + polymerize(x, b, depth-1)


count = sum(map(polymerize, pairs, pairs[1:]), Counter(pairs))
print(max(count.values()) - min(count.values()))
