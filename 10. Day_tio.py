# --- Day 10: Pipe Maze ---
#
# You use the hang glider to ride the hot air from Desert Island all the way up to the floating metal island. This island is surprisingly cold and there definitely aren't any thermals to glide on, so you leave your hang glider behind.
#
# You wander around for a while, but you don't find any people or animals. However, you do occasionally find signposts labeled "Hot Springs" pointing in a seemingly consistent direction; maybe you can find someone at the hot springs and ask them where the desert-machine parts are made.
#
# The landscape here is alien; even the flowers and trees are made of metal. As you stop to admire some metal grass, you notice something metallic scurry away in your peripheral vision and jump into a big pipe! It didn't look like any animal you've ever seen; if you want a better look, you'll need to get ahead of it.
#
# Scanning the area, you discover that the entire field you're standing on is densely packed with pipes; it was hard to tell at first because they're the same metallic silver color as the "ground". You make a quick sketch of all of the surface pipes you can see (your puzzle input).
#
# The pipes are arranged in a two-dimensional grid of tiles:
#
#     | is a vertical pipe connecting north and south.
#     - is a horizontal pipe connecting east and west.
#     L is a 90-degree bend connecting north and east.
#     J is a 90-degree bend connecting north and west.
#     7 is a 90-degree bend connecting south and west.
#     F is a 90-degree bend connecting south and east.
#     . is ground; there is no pipe in this tile.
#     S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
#
# Based on the acoustics of the animal's scurrying, you're confident the pipe that contains the animal is one large, continuous loop.
#
# For example, here is a square loop of pipe:
#
# .....
# .F-7.
# .|.|.
# .L-J.
# .....
#
# If the animal had entered this loop in the northwest corner, the sketch would instead look like this:
#
# .....
# .S-7.
# .|.|.
# .L-J.
# .....
#
# In the above diagram, the S tile is still a 90-degree F bend: you can tell because of how the adjacent pipes connect to it.
#
# Unfortunately, there are also many pipes that aren't connected to the loop! This sketch shows the same loop as above:
#
# -L|F7
# 7S-7|
# L|7||
# -L-J|
# L|-JF
#
# In the above diagram, you can still figure out which pipes form the main loop: they're the ones connected to S, pipes those pipes connect to, pipes those pipes connect to, and so on. Every pipe in the main loop connects to its two neighbors (including S, which will have exactly two pipes connecting to it, and which is assumed to connect back to those two pipes).
#
# Here is a sketch that contains a slightly more complex main loop:
#
# ..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ...
#
# Here's the same example sketch with the extra, non-main-loop pipe tiles also shown:
#
# 7-F7-
# .FJ|7
# SJLL7
# |F--J
# LJ.LJ
#
# If you want to get out ahead of the animal, you should find the tile in the loop that is farthest from the starting position. Because the animal is in the pipe, it doesn't make sense to measure this by direct distance. Instead, you need to find the tile that would take the longest number of steps along the loop to reach from the starting point - regardless of which way around the loop the animal went.
#
# In the first example with the square loop:
#
# .....
# .S-7.
# .|.|.
# .L-J.
# .....
#
# You can count the distance each tile in the loop is from the starting point like this:
#
# .....
# .012.
# .1.3.
# .234.
# .....
#
# In this example, the farthest point from the start is 4 steps away.
#
# Here's the more complex loop again:
#
# ..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ...
#
# Here are the distances for each tile on that loop:
#
# ..45.
# .236.
# 01.78
# 14567
# 23...
#
# Find the single giant loop starting at S. How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?
#
# To begin, get your puzzle input.

import copy
# Variables
answer, score = 0, 0
# file = 'Inputs/Day_10_test_input'  # test
file = 'Inputs/Day_10_input'  # prod
direction_options = {
    'north': ['|', '7', 'F', 'S'],
    'east':  ['-', '7', 'J', 'S'],
    'south': ['|', 'J', 'L', 'S'],
    'west':  ['-', 'L', 'F', 'S']
}
pipe_options = {
    '|': ['north', 'south'],
    '-': ['east', 'west'],
    'L': ['north', 'east'],
    'J': ['north', 'west'],
    '7': ['south', 'west'],
    'F': ['south', 'east'],
    'S': ['north', 'east', 'south', 'west']
}

# Read file
with open(file, 'r') as reader:
    maze_list = reader.readlines()

maze = list()
for line in maze_list:
    line = list(line.rstrip())
    maze.append(line[:])

def visualize_maze(maze_to_print):
    maze_to_print = copy.deepcopy(maze_to_print)
    # Add Y axis
    y = 0
    for rows in maze_to_print:
        y_str = str(y)
        rows.insert(0, y_str)
        y += 1
    # Add X axis
    x = 0
    x_axis = list('&')
    for column in range(len(maze_to_print[0]) - 1):
        x_str = str(x)
        x_axis.append(x_str)
        x += 1
    maze_to_print.insert(0, x_axis)

    row_print = list()
    for rows in maze_to_print:
        for char in rows:
            char_print = char.replace('|', '║').replace('7','╗').replace('F','╔').replace('J','╝').replace('L','╚').replace('-','═').replace('S','╬')
            row_print.append(char_print)
        print(*row_print,sep =' ')
        row_print.clear()
    maze_to_print.clear()
    x_axis.clear()

visualize_maze(maze)

# Find start
def find_start():
    start_x = 0
    start_y = 0
    for row in maze:
        if 'S' in row:
            start_x = row.index('S')
            break
        start_y += 1
    f_start_location = ['S', [start_x, start_y], [-1, -1]]
    return f_start_location

# Find points around location
def possible_ways(p_location):
    tunnel_piece = p_location[0]
    f_location = p_location[1]
    old_location = p_location[2]
    new_locations = list()
    # Scout locations
    if 'north' in pipe_options[tunnel_piece]:
        north = [maze[f_location[1] - 1][f_location[0]], [f_location[0], f_location[1] - 1]]
        if (            north[0] != '.'
                    and [f_location[0], f_location[1] - 1] != old_location
        ):
            new_locations.append(north)
    if 'east' in pipe_options[tunnel_piece]:
        east =  [maze[f_location[1]][f_location[0] + 1], [f_location[0] + 1, f_location[1]]]
        if (        east[0] != '.'
                and [f_location[0] + 1, f_location[1]] != old_location
        ):
            new_locations.append(east)
    if 'south' in pipe_options[tunnel_piece]:
        south = [maze[f_location[1] + 1][f_location[0]], [f_location[0], f_location[1] + 1]]
        if (
                    south[0] != '.'
                and [f_location[0], f_location[1] + 1] != old_location
        ):
            new_locations.append(south)
    if 'west' in pipe_options[tunnel_piece]:
        west =  [maze[f_location[1]][f_location[0] - 1], [f_location[0] - 1, f_location[1]]]
        if (
                    west[0] != '.'
                and [f_location[0] - 1, f_location[1]] != old_location
        ):
            new_locations.append(west)

    new_locations = new_locations[0]
    new_locations.append(f_location) # the new old location
    return new_locations

start_location = find_start()
print(f'Starting point: X, Y = {start_location[1]}')

location = possible_ways(start_location)
print(f'Possible ways: {location}')

# Move to new location
step = 0
while True:
    if location[0] == 'S': break
    location = possible_ways(location)
    step += 1

answer = int(step / 2) + (step % 2 > 0)
print(f'Number of total steps: {step}. Devided by 2 rounded up {answer}')