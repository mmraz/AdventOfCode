#!/usr/bin/env python3

import re

inputs = []
results = []
DEBUG = False

with open('input', 'r') as f:
    inputs = f.read().splitlines()


nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
nums_re = re.compile(r'(?=(\d|%s))' % '|'.join(nums))

for line in inputs:
    digits = []
    for num in nums_re.findall(line):
        if num in nums:
            num = str(nums.index(num) + 1)
        digits.append(num)
    results.append(int(f'{digits[0]}{digits[-1]}'))
if DEBUG:
    print(results)

print(sum(results))
