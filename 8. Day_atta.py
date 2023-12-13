# --- Day 8: Haunted Wasteland ---
#
# You're still riding a camel across Desert Island when you spot a sandstorm quickly approaching. When you turn to warn the Elf, she disappears before your eyes! To be fair, she had just finished warning you about ghosts a few minutes ago.
#
# One of the camel's pouches is labeled "maps" - sure enough, it's full of documents (your puzzle input) about how to navigate the desert. At least, you're pretty sure that's what they are; one of the documents contains a list of left/right instructions, and the rest of the documents seem to describe some kind of network of labeled nodes.
#
# It seems like you're meant to use the left/right instructions to navigate the network. Perhaps if you have the camel follow the same instructions, you can escape the haunted wasteland!
#
# After examining the maps for a bit, two nodes stick out: AAA and ZZZ. You feel like AAA is where you are now, and you have to follow the left/right instructions until you reach ZZZ.
#
# This format defines each node of the network individually. For example:
#
# RL
#
# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)
#
# Starting with AAA, you need to look up the next element based on the next left/right instruction in your input. In this example, start with AAA and go right (R) by choosing the right element of AAA, CCC. Then, L means to choose the left element of CCC, ZZZ. By following the left/right instructions, you reach ZZZ in 2 steps.
#
# Of course, you might not find ZZZ right away. If you run out of left/right instructions, repeat the whole sequence of instructions as necessary: RL really means RLRLRLRLRLRLRLRL... and so on. For example, here is a situation that takes 6 steps to reach ZZZ:
#
# LLR
#
# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)
#
# Starting at AAA, follow the left/right instructions. How many steps are required to reach ZZZ?

answer = 0
# file = 'Inputs/Day_8_test_input'  # test
file = 'Inputs/Day_8_input'  # prod

# Purge empty lines and fill list.
with open(file, 'r') as reader, open(file, 'r+') as writer:
    for line in reader:
        if line.strip():
            writer.write(line)
    writer.truncate()

with open(file, 'r') as reader:
    line_list = reader.readlines()

directions_list = list()
node_dict = {}
for l in line_list:
    if len(directions_list) == 0:
        directions_list = list(l.strip().replace('L', '0').replace('R', '1'))
    else:
        l = l.replace(' = ', ',').replace('(','').replace(')','').replace(', ', ',').strip().split(',')
        node_dict[l[0]] = [l[1], l[2]]
print(f'The node_dict: {node_dict}')
print(f'The directions: {directions_list}')

destination_location = 'AAA'
nr_directions = len(directions_list) - 1
direction = directions_list[0]
i = 0
tries = 0

# while current_location != 'ZZZ':
while True:

    if destination_location == 'ZZZ': break
    else: tries += 1
    origin_location_list = node_dict[destination_location]
    origin_location = origin_location_list[int(direction)]
    if i < nr_directions:
        i += 1
    else: i = 0
    direction = directions_list[i]

    if origin_location == 'ZZZ': break
    else: tries += 1
    destination_location_list = node_dict[origin_location]
    destination_location = destination_location_list[int(direction)]
    if i < nr_directions:
        i += 1
    else: i = 0
    direction = directions_list[i]

print(tries)
# 16697
