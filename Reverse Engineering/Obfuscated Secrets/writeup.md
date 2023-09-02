# Obfuscated Secrets
> Solves - 0

## Description
Our secret agent John T P has stolen some secret info from the enemy _mill_ but had to obscure it to sneak it out. Sadly John forgot what he did. Can you get it back?

## Hint
1. `25 PT` - Wonder what languages they use at a mill? Must be some Go0d 1  

## Files Attached
- [main.py](./main.py)
- [output](./output)

## Solution

- Go through `main.py`

- Understand the 3 functions applied on the input file
    - Removing first 4 characters of each line
    - Every 5 elements, lines are reversed
    - Float XOR with key `0xEC`, applied on number X (possible coordinate?)

- From descripton, mentions enemy mill, on searching, popular languages at mills include GCODE for CNC machines.

- Scouting through GCODE codes, most seem to be starting with `G01 ` which could be possible characters trimmed

- Reverse functions, append G01

- Create script to reverse - [solution.py](./solution.py)

- View generated code through any GCODE online viewers
![GCODE Output](../../Images/gcode.png)

## Flag
>`pesu_ec{f0r_d3M_pr3s15e_cut5}`

## Fun Fact
John T P or John T. Parsons was the first person to invent and build an NC (Numerical Control) machine. The NC machine was designed to operate directly off a set of punch cards that tell the machine where to move.
