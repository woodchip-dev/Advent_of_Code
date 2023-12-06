# Advent of Code

## Project Structure
<pre>
2020/  
    |---- day_01/  
        |----> part_a.py  
        |----> part_b.py
    |---- day_02/  
        |----> part_a.py  
        |----> part_b.py
    |---- ...
    |---- input_files/  
        |----> aoc_01.txt  
        |----> aoc_02.txt  
        |----> ...  
2021/  
    |---- ...  
.../  
utils/  
    |----> __init__.py  
    |----> input_handler.py  
    |----> output_handler.py  
</pre>

## Getting Started

### Install Prerequisites
`sudo apt-get install python3 python3-pip python3-venv`  

### Initial Setup
1. Navigate to Advent_of_Code/  
2. Run `python3 -m venv env`  
3. Run `source setup.sh`  

### Subsequent Setup
1. Run `source setup.sh`  

### How To Run day_[0-9]{2} part_[ab] of Year 20[0-9]{2}
1. Navigate to Advent_of_Code/, if not already there  
2. Run `python3 -m 20[0-9]{2}.day_[0-9]{2}.part_[ab]`  
Example: for day\_05 part\_a in 2022, it would be `python3 -m 2022.day_05.part_a`  

