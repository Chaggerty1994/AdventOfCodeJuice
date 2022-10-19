from more_itertools import pairwise
import pathlib



# declaring a a variable and setting 
# its value to the given input data
# the result is a string

input_one = pathlib.Path('step_one.txt').read_text().rstrip()

input_two = pathlib.Path('step_two.txt').read_text().rstrip()

# turning that string into a list of strings

lines = input_two.rstrip().split('\n')


# converting the list of numbers as strings to a list of integers
lines_to_numbers = [int(line) for line in lines]

# using pairwise to divide the list into pairs
# iterate the list of pairs
# if b is greater than a return true, else false
depth_increases = [b > a for a, b in pairwise(lines_to_numbers)]

# count the number of true booleans in depth_increases
print(sum(depth_increases))