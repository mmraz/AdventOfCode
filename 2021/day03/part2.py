#!/usr/bin/env python3

DEBUG = False

with open('input', 'r') as f:
    inputs = f.read().splitlines()

data = [int(entry, 2) for entry in inputs]

bitw = len(inputs[0])
if DEBUG:
    print(f"bit width {bitw}")

def parse(data, width, least=False):
    # start at least significant bit and step back
    for i in range(width-1,-1,-1):
        count = 0
        for f in data:
            count += f >> i & 1
        about_half =  len(data)//2 + len(data)%2
        if least:
            count = count < about_half
        else:
            count = count >= about_half
        data = [x for x in data if x>>i & 1 == count]
        if DEBUG:
            print(f"data length {len(data)}")
        if len(data) == 1:
            return data.pop()

# duplicate data list as it's filtered in place during parsing
datac = data.copy()
cotwo = parse(data, bitw, True)
oxygen = parse(datac, bitw)
print(oxygen * cotwo)
