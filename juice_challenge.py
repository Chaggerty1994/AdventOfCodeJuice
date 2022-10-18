
import pathlib



# declaring a a variable and setting 
# its value to the given input data
# the result is a string

input = pathlib.Path('step_one.txt').read_text().rstrip()

print(input)

# turning that string into a list of strings

lines = input.rstrip().split('\n')

# converting the list of numbers as strings to a list of integers
lines_to_numbers = [int(line) for line in lines]

print(lines_to_numbers)

# for a, b in permutations(lines_to_numbers)

