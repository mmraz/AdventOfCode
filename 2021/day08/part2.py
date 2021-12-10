#!/usr/bin/env python3

inputs = list()
DEBUG = False

with open('input', 'r') as f:
    inputs = f.read().splitlines()

jumbled = [[set(i) for i in line.split()] for line in inputs]


total = 0
for zrt in jumbled:
    segments = sorted(zrt[:10], key=len)
    if DEBUG:
        print(f"zrt {zrt}\nsegments sorted {segments}")
    segments[3:6] = sorted(segments[3:6], key=lambda x: (segments[1].issubset(x), len(segments[2] & x)))
    segments[6:9] = sorted(segments[6:9], key=lambda x: (segments[2].issubset(x), segments[1].issubset(x)))
    segments = [segments[x] for x in (7, 0, 3, 5, 2, 4, 6, 1, 9, 8)]
    if DEBUG:
        print(f"segments mapped {segments}")

    result = ''
    for digit in zrt[-4:]:
        for i, segment in enumerate(segments):
            if segment == digit:
                result += str(i)
    total += int(result)
print(total)
