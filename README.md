# AdventOfCode2021
Personal solutions to the 2021 Advent of Code puzzles for [Michael Mraz](https://github.com/mmraz)

## Automation
All code reads inputs from a file named `input` and prints the answer to STDOUT

Interaction with the website is done using [aoc-cli](https://github.com/scarvalhojr/aoc-cli)

```
cd day##
aoc read -d ##
aoc download -d ##
aoc submit 1 $(./part1.py) -d ## 
aoc submit 2 $(./part2.py) -d ## 
```
## Templates

There are starter template files for several languages to read the `input`
into a variable.  Copy one for your language of choice into the day's
directory as an easy starting point for your solution.

## Support Advent of Code

Advent of Code is a free online Advent calendar of small programming puzzles
created by [Eric Wastl](http://was.tl/) and maintained by volunteers. Please
consider [supporting their work](https://adventofcode.com/support).
