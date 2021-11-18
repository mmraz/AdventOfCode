#!/usr/bin/env python3

inputs = ''
DEBUG = 0

with open('input', 'r') as f:
    inputs = f.read().splitlines()

expenses = [int(v) for v in inputs]
res = [ele for ele in expenses if( (2020 - ele) in expenses)]
print(res[0] * res[1])
