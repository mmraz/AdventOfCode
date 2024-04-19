# AdventOfCode
Personal solutions to the Advent of Code puzzles for [Michael Mraz](https://github.com/mmraz)

## Automation
All code reads inputs from a file named `input` and prints the answer to STDOUT

Interaction with the website is done using [aoc-cli](https://github.com/scarvalhojr/aoc-cli)

```
cd <year>/day##
aoc read 1 -y <year> -d ##
aoc download -y <year> -d ##
aoc submit 1 $(./part1.py) -y <year> -d ## 
aoc submit 2 $(./part2.py) -y <year> -d ## 
```
## Templates

There are starter template files for several languages to read the `input`
into a variable.  Copy one for your language of choice into the day's
directory as an easy starting point for your solution.

## Support Advent of Code

Advent of Code is a free online Advent calendar of small programming puzzles
created by [Eric Wastl](http://was.tl/) and maintained by volunteers. Please
consider [supporting their work](https://adventofcode.com/support).

