# The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.
#
# The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)
#
# Here is an example engine schematic:

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

# In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.
#
# Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

answer = 0
engine_2d_list = []

file = open('Inputs/Day_3_test_input', 'r')
line_list = file.readlines()
y = 0
x_axis_list = list('&')
coord_list = list()

# Add X and Y axis
for line in line_list:
    line = line.rstrip()
    xx = list(line)
    y_str = str(y)
    xx.insert(0, y_str)
    engine_2d_list.append(xx)
    x_axis_list.append(y_str)
    y += 1
engine_2d_list.insert(0, x_axis_list)

# print engine
for line in engine_2d_list:
    print(line)

# Find all special characters and note coordinates
for line in engine_2d_list:
    y_axis = line[0]
    x_axis = -1
    if y_axis == '&':  # skip header
        continue
    for char in line:
        if not char.isdigit() and char != '.':
            coord = str(x_axis) + ',' + y_axis
            coord_list.append(coord)
            # print(f'Found special char = {char} on X= {x_axis} Y= {y_axis}')
        x_axis += 1
print(f'Coordinate list = {coord_list}')

for coord in coord_list:
    x_coord = int(coord[0]) + 1
    y_coord = int(coord[2]) + 1
    print(f'Search around {engine_2d_list[y_coord][x_coord]} at X= {x_coord} and Y= {y_coord}')
    left_top_corner = engine_2d_list[y_coord - 1][x_coord - 1]
    top_mid = engine_2d_list[y_coord - 1][x_coord]
    right_top_corner = engine_2d_list[y_coord + 1][x_coord + 1]
    right = engine_2d_list[y_coord][x_coord + 1]
    right_bottom_corner = engine_2d_list[y_coord + 1][x_coord + 1]
    bottem_mid = engine_2d_list[y_coord + 1][x_coord]
    left_bottem_corner = engine_2d_list[y_coord + 1][x_coord - 1]
    left = engine_2d_list[y_coord][x_coord - 1]




