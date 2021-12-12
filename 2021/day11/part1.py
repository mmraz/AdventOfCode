#!/usr/bin/env python3
import numpy as np

DEBUG = False

octopi = np.genfromtxt('input', delimiter=1)
if DEBUG:
    print(octopi)


def blast_radius(i, j):
    return np.array([[i+di, j+dj]for dj in range(-1, 2) for di in range(-1, 2) if not ((dj == 0) and (di == 0))])


def propogate_flashes(octopi):
    dead_batteries = np.zeros_like(octopi).astype(bool)
    octopi = octopi.copy()
    while (octopi[~dead_batteries] > 9).sum():
        flashing = np.transpose(np.nonzero((octopi > 9) & (~dead_batteries)))
        for i, j in flashing:
            to_update = blast_radius(i, j)
            octopi[to_update[:, 0], to_update[:, 1]] += 1
            dead_batteries[i, j] = True

    return octopi


def flash_dance(octopi):
    octopi = octopi.copy()
    octopi = octopi+1
    octopi = propogate_flashes(octopi)
    dead_batteries = octopi > 9
    octopi[dead_batteries] = 0
    return octopi, dead_batteries.sum()


# pad around the edges with a value that never will flash
octopi = np.pad(octopi, 1, constant_values=-np.inf)
total = 0
for _ in range(0, 100):
    octopi, num_flashed = flash_dance(octopi)
    total += num_flashed
    if DEBUG:
        print(f"day {_} flashed {num_flashed}")

print(total)
