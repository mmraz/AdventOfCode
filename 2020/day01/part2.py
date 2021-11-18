#!/usr/bin/env python3
from itertools import *
from math import prod

inputs = ''
DEBUG = 0

with open('input', 'r') as f:
    inputs = f.read().splitlines()

expenses = [int(v) for v in inputs]
expense_pairs = list(combinations(expenses, 3))

def sums_to_2020(values):
    return sum(values) == 2020

result = list(filter(sums_to_2020, expense_pairs))
if(DEBUG): print(result)
print(prod(result[0]))
