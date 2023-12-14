
# Solutions for AdventOfCode2023

I have tried to provide a solution for AdventOfCode2023 with my test cases in Python

## Solutions

| Day | Problem1 | Problem2 |
| :-- | :------: | :------: |
| [day1](https://adventofcode.com/2023/day/1) | [part1](https://github.com/anmol1115/AdventOfCode2023/blob/main/day1/part1.py)   | [part2](https://github.com/anmol1115/AdventOfCode2023/blob/main/day1/part2.py)    |
| [day2](https://adventofcode.com/2023/day/2) | [part1](https://github.com/anmol1115/AdventOfCode2023/blob/main/day2/part1.py)   | [part2](https://github.com/anmol1115/AdventOfCode2023/blob/main/day2/part2.py)    |
| [day3](https://adventofcode.com/2023/day/3) | [part1](https://github.com/anmol1115/AdventOfCode2023/blob/main/day3/part1.py)   | [part2](https://github.com/anmol1115/AdventOfCode2023/blob/main/day3/part2.py)    |
| [day4](https://adventofcode.com/2023/day/4) | [part1](https://github.com/anmol1115/AdventOfCode2023/blob/main/day4/part1.py)   | [part2](https://github.com/anmol1115/AdventOfCode2023/blob/main/day4/part2.py)    |
| [day5](https://adventofcode.com/2023/day/5) | [part1](https://github.com/anmol1115/AdventOfCode2023/blob/main/day5/part1.py)   ||
| [day6](https://adventofcode.com/2023/day/6) | [part1](https://github.com/anmol1115/AdventOfCode2023/blob/main/day6/part1.py)   | [part2](https://github.com/anmol1115/AdventOfCode2023/blob/main/day6/part2.py)    |
| [day7](https://adventofcode.com/2023/day/7) | [part1](https://github.com/anmol1115/AdventOfCode2023/blob/main/day6/part2.py)   | [part2](https://github.com/anmol1115/AdventOfCode2023/blob/main/day7/part2.py)    |
| [day8](https://adventofcode.com/2023/day/8) | [part1](https://github.com/anmol1115/AdventOfCode2023/blob/main/day8/part1.py)   | [part2](https://github.com/anmol1115/AdventOfCode2023/blob/main/day8/part2.py)    |
| [day9](https://adventofcode.com/2023/day/9) | [part1](https://github.com/anmol1115/AdventOfCode2023/blob/main/day9/part1.py)   | [part2](https://github.com/anmol1115/AdventOfCode2023/blob/main/day9/part2.py)    |
| [day10](https://adventofcode.com/2023/day/10) | [part1](https://github.com/anmol1115/AdventOfCode2023/blob/main/day10/part1.py)   ||
| [day11](https://adventofcode.com/2023/day/11) | [part1](https://github.com/anmol1115/AdventOfCode2023/blob/main/day11/part1.py)   ||

## Intution
___
### Day1-Part1
Check from left, if a number is found added it as msb. Similarly checking from right hand side, adde number as lsb.

### Day1-Part2
Convert all spelled out numbers into digits and run the same algo as in part1.
___
### Day2-Part1
Compare each game with the given threshold of `{'red': 12, 'green': 13, 'blue': 14}` balls.

### Day2-Part2
Take the maximum of each color of ball for each game to find the least number of balls available.
___
### Day3-part1
For each number in given input check all neighbouring values, if a special character is present, add to sum.

### Day3-part2
For each `*` symbol present create a set of neighbouring numbers and multiply the numbers where lenght of the set is 2. To avoid duplicate/multiple same entries set is used and to avoid missing two same values we use index as well while saving in set.
___
### Day4-part1
Find number of common elements in given numbers and winning numbers. Add to sum the 2's power of the count.

### Day4-part2
Maintain a cache with 1 depicting 1 card at the beginning. Calculating count the same way as in part 1, we update cache for that many cards after current card.
___
### Day5-part1
Calculate location value for each seed-range and find minimum of those locations.
___
### Day6-part1
For every given time since the speed of boat is same as the time for which the button is held down, this means if the button is held for x seconds, the time availble is (t-x) seconds. Calculate product where the record can be beaten.

### Day6-part2
Using the same logic as in part1, just combine the given times and distances.
___
### Day7-part1
Sort the different card hands based on first the hand type then card type. Here Ive created a class for a card hand and created a priority list, with first value as the hand type and second as card type. Sorting uses these priority list as key.

### Day7-part2
Update the priority of 'J' Card in Card priority map. For any hand having 'J' cards, 'J' cards are converted to type of card which has the largest count. Then priority list is calculated for the updated hand.
___
### Day8-part1
Starting from 'AAA' loop through the map following the directions till 'ZZZ' is not reached.

### Day8-part2
Calculate length of path for each starting values ending with 'A' and ending values ending with 'Z' and calculate the least common multiple for all these values.
___
### Day9-part1
For each list in input, recursively find the list where each value is zero, from that point return recursive value received + the last value of list passed to that recursive fn.

### Day9-part2
For each list in input, recursively find the list where each value is zero, from that point return the first value of list passed to that recursive fn - recursive value received.
___
### Day10-part1
Since it is given that the there is a closed loop, we travel from one path end to the other path end and count the total steps. Finally divide the number of steps by 2 to get to the farthest point.
___
### Day11-part1
To expand the list, expand each row, and for expanding the columns transpose the list. Find the manhatten distance between each point, for the extended list.