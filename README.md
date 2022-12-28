# Advent of Code

Collection of the code for the solutions to the various advent of code problems

## Usage
The process makes use of `wrapper.py` to help reduce the amount of boilerplate required to read the input file and process its lines
1. Running `wrapper.py dayNumber` (where dayNumber is a 2-digit int) will initialise the dircetory and copy the `template.py` in as `solution.py`
1. Running `wrapper.py dayNumber` will execute the code in the newly created `dayNumber/solution.py` file
1. Running `wrapper.py dayNumber solutionPart` (where solution part is either 1 or 2) will execute the code in the relevant block within `solution.py`

