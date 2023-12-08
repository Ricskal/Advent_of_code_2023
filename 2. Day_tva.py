# --- Day 2: Cube Conundrum ---
# As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.
#
# To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.
#
# You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).
#
# For example, the record of a few games might look like this:
#
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
#
# In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.
#
# The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
#
# In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.
#
# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

answer = 0
red_dice = 0
green_dice = 0
blue_dice = 0
set_possible = []

file = open('Inputs/Day_2_input', 'r')
line_list = file.readlines()

for line in line_list:
    x = line.split(':')
    game_number = int(x[0][4:])
    game = x[1]
    game_sets = game.split(';')
    number_of_game_sets = len(game_sets)
    print(f'The game {game_number} contains {number_of_game_sets} sets = {game_sets}')

    for sets in game_sets:
        y = sets.strip().split(',')

        for z in y:
            w = z.strip()
            if w.find('red') != -1:
                red_dice += int(w[0:2])
            elif w.find('green') != -1:
                green_dice += int(w[0:2])
            elif w.find('blue') != -1:
                blue_dice += int(w[0:2])

        if red_dice <= 12 and green_dice <= 13 and blue_dice <= 14:
            print(f'The set {y} from game {game_number} is possible')
            set_possible.append(True)
        else:
            print(f'The set {y} from game {game_number} is NOT possible')
            set_possible.append(False)

        red_dice = 0
        green_dice = 0
        blue_dice = 0

    game_possible = False
    for possibilities in set_possible:
        if possibilities:
            game_possible = True
        else:
            game_possible = False
            break

    if game_possible:
        print(f'The answer was {answer}, game {game_number} is possible and will be added. New answer {answer + game_number}')
        answer += game_number
    else:
        print(f'The answer was {answer}, game {game_number} is NOT possible and will NOT be added. The answer remains {answer}')

    print()
    set_possible.clear()
    red_dice = 0
    green_dice = 0
    blue_dice = 0

print(f'The answer = {answer}')










