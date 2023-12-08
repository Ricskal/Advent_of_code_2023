# --- Day 3: Gear Ratios ---
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
answer_dict = {}
engine_2d_list = []
file = open('Inputs/Day_3_input', 'r')
line_list = file.readlines()
y = 0
x_axis_list = list('&')
coord_list_chars = list()
coord_dict_numbers = {}

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
    if y_axis == '&':  # skip x-axis
        continue
    for char in line:
        if char == '*':
            coord_chars = str(x_axis) + ',' + y_axis
            coord_list_chars.append(coord_chars)
            print(f'Found a gear = {char} on X= {x_axis} Y= {y_axis}')
        x_axis += 1
print(f'Coordinate list special characters X,Y = {coord_list_chars}')

# Find all numbers and note coordinates
digit = ''
coord_numbers = ''
y_axis_skipped = False
number_started = False
for line in engine_2d_list:
    y_axis = line[0]
    x_axis = 0
    if y_axis == '&':  # skip x-axis
        continue
    for char in line:
        if char == y_axis and not y_axis_skipped:  # skip y-axis
            y_axis_skipped = True
            continue
        if char.isdigit():
            digit = digit + char
            coord_numbers = coord_numbers + str(x_axis) + ',' + y_axis + '|'
            number_started = True
        elif not char.isdigit() and number_started:
            coord_dict_numbers[coord_numbers[:-1]] = digit
            number_started = False
            digit = ''
            coord_numbers = ''
        x_axis += 1
    if number_started:
        coord_dict_numbers[coord_numbers[:-1]] = digit
        number_started = False
        digit = ''
        coord_numbers = ''
    digit = ''
    coord_numbers = ''
    y_axis_skipped = False
    number_started = False
print(f'Coordinate list numbers X,Y = {coord_dict_numbers}')

# Find surrounding coordinates from special chars and cross with coordinates of numbers
for coord_char in coord_list_chars:
    coord_char_list = coord_char.split(',')
    x_coord = int(coord_char_list[0])
    y_coord = int(coord_char_list[1])
    print(f'Search around {engine_2d_list[y_coord + 1][x_coord + 1]} at X= {x_coord} and Y= {y_coord}')
    left_top_corner = str(x_coord - 1) + ',' + str(y_coord - 1)
    top_mid = str(x_coord) + ',' + str(y_coord - 1)
    right_top_corner = str(x_coord + 1) + ',' + str(y_coord - 1)
    right = str(x_coord + 1) + ',' + str(y_coord)
    right_bottom_corner = str(x_coord + 1) + ',' + str(y_coord + 1)
    bottem_mid = str(x_coord) + ',' + str(y_coord + 1)
    left_bottem_corner = str(x_coord - 1) + ',' + str(y_coord + 1)
    left = str(x_coord - 1) + ',' + str(y_coord)
    surrounding_list = (left_top_corner, top_mid, right_top_corner, right, right_bottom_corner, bottem_mid, left_bottem_corner, left)
    print(f'Serrounding coordinates = {surrounding_list}')

    number_of_sets = 0
    for coord_surr in surrounding_list:
        for key in coord_dict_numbers:
            key_list = key.split('|')
            for keys in key_list:
                if coord_surr == keys:
                    number_of_sets += 1
                    if number_of_sets == 1:
                        set1 = coord_dict_numbers[key]
                        set1_key = key
                    elif number_of_sets == 2 and key == set1_key:
                        number_of_sets = 1
                    elif number_of_sets == 2 and key != set1_key:
                        set2 = coord_dict_numbers[key]
                        set2_key = key
                        gear_ratio_key = set1_key + ' - ' + set2_key
                        gear_ratio = int(set1) * int(set2)
                        number_of_sets += 1
                        answer_dict[gear_ratio_key] = gear_ratio
                    elif number_of_sets > 2:
                        if key == set1_key or key == set2_key:
                            print('It\'s the same number!')
                        else:
                            print('More then 2 numbers!, delete >:D')
                            answer_dict.pop(gear_ratio_key, None)

print(answer_dict)
for answers in answer_dict.values():
    answer += int(answers)
print(answer)












