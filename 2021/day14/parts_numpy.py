#!/usr/bin/env python3
import numpy as np

DEBUG = False

with open('input.ex', 'r') as f:
    inputs = f.read().splitlines()

rules = dict([line.split(' -> ') for line in inputs[2:]])
ridx = dict(zip(rules, range(len(rules))))
mat = np.zeros((len(rules), len(rules)), dtype=object)
for p in rules:
    mat[ridx[p[0] + rules[p]]][ridx[p]] = 1
    mat[ridx[rules[p] + p[1]]][ridx[p]] = 1
tmp = list(zip(inputs[0], inputs[0][1:]))
v = [tmp.count((p[0], p[1])) for p in rules]
for pow in [10, 40]:
    w = np.dot(np.linalg.matrix_power(mat, pow), v)
    cnt = {inputs[0][0]: 1}
    for p in ridx:
        cnt[p[1]] = cnt.get(p[1], 0) + w[ridx[p]]
    lmin = min(cnt, key=lambda k: cnt[k])
    lmax = max(cnt, key=lambda k: cnt[k])
    print(cnt[lmax]-cnt[lmin])
