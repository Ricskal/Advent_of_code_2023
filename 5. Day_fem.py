# --- Day 5: If You Give A Seed A Fertilizer ---
#
# The almanac (your puzzle input) lists all of the seeds that need to be planted. It also lists what type of soil to use with each kind of seed, what type of fertilizer to use with each kind of soil, what type of water to use with each kind of fertilizer, and so on. Every type of seed, soil, fertilizer and so on is identified with a number, but numbers are reused by each category - that is, soil 123 and fertilizer 123 aren't necessarily related to each other.
#
# For example:
#
# seeds: 79 14 55 13
#
# seed-to-soil map:
# 50 98 2
# 52 50 48
#
# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15
#
# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4
#
# water-to-light map:
# 88 18 7
# 18 25 70
#
# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13
#
# temperature-to-humidity map:
# 0 69 1
# 1 0 69
#
# humidity-to-location map:
# 60 56 37
# 56 93 4
#
# The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.
#
# The rest of the almanac contains a list of maps which describe how to convert numbers from a source category into numbers in a destination category. That is, the section that starts with seed-to-soil map: describes how to convert a seed number (the source) to a soil number (the destination). This lets the gardener and his team know which soil to use with which seeds, which water to use with which fertilizer, and so on.
#
# Rather than list every source number and its corresponding destination number one by one, the maps describe entire ranges of numbers that can be converted. Each line within a map contains three numbers: the destination range start, the source range start, and the range length.
#
# Consider again the example seed-to-soil map:
#
# 50 98 2
# 52 50 48
#
# The first line has a destination range start of 50, a source range start of 98, and a range length of 2. This line means that the source range starts at 98 and contains two values: 98 and 99. The destination range is the same length, but it starts at 50, so its two values are 50 and 51. With this information, you know that seed number 98 corresponds to soil number 50 and that seed number 99 corresponds to soil number 51.
#
# The second line means that the source range starts at 50 and contains 48 values: 50, 51, ..., 96, 97. This corresponds to a destination range starting at 52 and also containing 48 values: 52, 53, ..., 98, 99. So, seed number 53 corresponds to soil number 55.
#
# Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.
#
# So, the entire list of seed numbers and their corresponding soil numbers looks like this:
#
# seed  soil
# 0     0
# 1     1
# ...   ...
# 48    48
# 49    49
# 50    52
# 51    53
# ...   ...
# 96    98
# 97    99
# 98    50
# 99    51
#
# With this map, you can look up the soil number required for each initial seed number:
#
#     Seed number 79 corresponds to soil number 81.
#     Seed number 14 corresponds to soil number 14.
#     Seed number 55 corresponds to soil number 57.
#     Seed number 13 corresponds to soil number 13.
#
# The gardener and his team want to get started as soon as possible, so they'd like to know the closest location that needs a seed. Using these maps, find the lowest location number that corresponds to any of the initial seeds. To do this, you'll need to convert each seed number through other categories until you can find its corresponding location number. In this example, the corresponding types are:
#
#     Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
#     Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
#     Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
#     Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
#
# So, the lowest location number in this example is 35.
#
# What is the lowest location number that corresponds to any of the initial seed numbers?

answer = 0
score = list()
file = open('Inputs/Day_5_input', 'r')
line_list = file.readlines()

seed_list_str = list()
seed_list = list()
seed_to_soil_started = False
seed_to_soil_map = list()
soil_to_fertilizer_started = False
soil_to_fertilizer_map = list()
fertilizer_to_water_started = False
fertilizer_to_water_map = list()
water_to_light_started = False
water_to_light_map = list()
light_to_temperature_started = False
light_to_temperature_map = list()
temperature_to_humidity_started = False
temperature_to_humidity_map = list()
humidity_to_location_map = list()

while '\n' in line_list:
    line_list.remove('\n')

for line in line_list:
    x = line.strip().split(' ')

    if x[0] == 'seeds:':
        seed_list_str = x[1::]
        for seed in seed_list_str:
            seed_list.append(int(seed))

    elif x[0] == 'seed-to-soil':
        seed_to_soil_started = True
        continue
    elif seed_to_soil_started and x[0] != 'soil-to-fertilizer':
        seed_to_soil_map.append(x)

    elif x[0] == 'soil-to-fertilizer':
        seed_to_soil_started = False
        soil_to_fertilizer_started = True
        continue
    elif soil_to_fertilizer_started and x[0] != 'fertilizer-to-water':
        soil_to_fertilizer_map.append(x)

    elif x[0] == 'fertilizer-to-water':
        soil_to_fertilizer_started = False
        fertilizer_to_water_started = True
        continue
    elif fertilizer_to_water_started and x[0] != 'water-to-light':
        fertilizer_to_water_map.append(x)

    elif x[0] == 'water-to-light':
        fertilizer_to_water_started = False
        water_to_light_started = True
        continue
    elif water_to_light_started and x[0] != 'light-to-temperature':
        water_to_light_map.append(x)

    elif x[0] == 'light-to-temperature':
        water_to_light_started = False
        light_to_temperature_started = True
        continue
    elif light_to_temperature_started and x[0] != 'temperature-to-humidity':
        light_to_temperature_map.append(x)

    elif x[0] == 'temperature-to-humidity':
        light_to_temperature_started = False
        temperature_to_humidity_started = True
        continue
    elif temperature_to_humidity_started and x[0] != 'humidity-to-location':
        temperature_to_humidity_map.append(x)

    elif x[0] == 'humidity-to-location':
        temperature_to_humidity_started = False
        continue
    else:
        humidity_to_location_map.append(x)

seed_to_soil_list = list()
for mapping in seed_to_soil_map:
    destination = int(mapping[0])
    source = int(mapping[1])
    mapping_range = int(mapping[2])
    start_source = source
    end_source = source + (mapping_range -1)
    offset = source - destination
    y1 = [start_source, end_source, offset]
    seed_to_soil_list.append(y1)

soil_to_fertilizer_list = list()
for mapping in soil_to_fertilizer_map:
    destination = int(mapping[0])
    source = int(mapping[1])
    mapping_range = int(mapping[2])
    start_source = source
    end_source = source + (mapping_range -1)
    offset = source - destination
    y2 = [start_source, end_source, offset]
    soil_to_fertilizer_list.append(y2)

fertilizer_to_water_list = list()
for mapping in fertilizer_to_water_map:
    destination = int(mapping[0])
    source = int(mapping[1])
    mapping_range = int(mapping[2])
    start_source = source
    end_source = source + (mapping_range -1)
    offset = source - destination
    y3 = [start_source, end_source, offset]
    fertilizer_to_water_list.append(y3)

water_to_light_list = list()
for mapping in water_to_light_map:
    destination = int(mapping[0])
    source = int(mapping[1])
    mapping_range = int(mapping[2])
    start_source = source
    end_source = source + (mapping_range -1)
    offset = source - destination
    y3 = [start_source, end_source, offset]
    water_to_light_list.append(y3)

light_to_temperature_list = list()
for mapping in light_to_temperature_map:
    destination = int(mapping[0])
    source = int(mapping[1])
    mapping_range = int(mapping[2])
    start_source = source
    end_source = source + (mapping_range -1)
    offset = source - destination
    y3 = [start_source, end_source, offset]
    light_to_temperature_list.append(y3)

temperature_to_humidity_list = list()
for mapping in temperature_to_humidity_map:
    destination = int(mapping[0])
    source = int(mapping[1])
    mapping_range = int(mapping[2])
    start_source = source
    end_source = source + (mapping_range -1)
    offset = source - destination
    y4 = [start_source, end_source, offset]
    temperature_to_humidity_list.append(y4)

humidity_to_location_list = list()
for mapping in humidity_to_location_map:
    destination = int(mapping[0])
    source = int(mapping[1])
    mapping_range = int(mapping[2])
    start_source = source
    end_source = source + (mapping_range -1)
    offset = source - destination
    y5 = [start_source, end_source, offset]
    humidity_to_location_list.append(y5)

print(f'''
Seed list: {seed_list}
Lists of all mappings:
- 1. seed-to-soil: {seed_to_soil_map}. Dict: {seed_to_soil_list}
- 2. soil-to-fertilizer: {soil_to_fertilizer_map}. Dict: {soil_to_fertilizer_list}
- 3. fertilizer_to_water: {fertilizer_to_water_map}. Dict: {fertilizer_to_water_list}
- 4. water-to-light: {water_to_light_map}. Dict: {water_to_light_list}
- 5. light-to-temperature: {light_to_temperature_map}. Dict: {light_to_temperature_list}
- 6. temperature-to-humidity: {temperature_to_humidity_map}. Dict: {temperature_to_humidity_list}
- 7. humidity-to-location: {humidity_to_location_map}. Dict: {humidity_to_location_list}
''')
found = False
for seed in seed_list:
    key = seed
    for mapping in seed_to_soil_list:
        if mapping[0] <= key <= mapping[1] and not found:
            key = (key - mapping[2])
            found = True
            continue

    found = False
    for mapping in soil_to_fertilizer_list:
        if mapping[0] <= key <= mapping[1] and not found:
            key = (key - mapping[2])
            found = True
            continue

    found = False
    for mapping in fertilizer_to_water_list:
        if mapping[0] <= key <= mapping[1] and not found:
            key = (key - mapping[2])
            found = True
            continue

    found = False
    for mapping in water_to_light_list:
        if mapping[0] <= key <= mapping[1] and not found:
            key = (key - mapping[2])
            found = True
            continue

    found = False
    for mapping in light_to_temperature_list:
        if mapping[0] <= key <= mapping[1] and not found:
            key = (key - mapping[2])
            found = True
            continue

    found = False
    for mapping in temperature_to_humidity_list:
        if mapping[0] <= key <= mapping[1] and not found:
            key = (key - mapping[2])
            found = True
            continue

    found = False
    for mapping in humidity_to_location_list:
        if mapping[0] <= key <= mapping[1] and not found:
            key = (key - mapping[2])
            found = True
            continue

    found = False
    score.append(key)

score.sort()
print(score)
print(score[0])
