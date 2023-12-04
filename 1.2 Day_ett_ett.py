# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
#
# For example:
#
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
#
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
#
# Consider your entire calibration document. What is the sum of all of the calibration values?
#
# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
#
# Equipped with this new information, you now need to find the real first and last digit on each line. For example:
#
# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
#
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
answer = 0

file = open('Inputs/Day_1_input', 'r')
line_list = file.readlines()
fline_list = []
fline_list_list = []
number_index = {}

number_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
number_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
number_list1 = ['one', '1', 'two', '2', 'three', '3', 'four', '4', 'five', '5', 'six', '6', 'seven', '7', 'eight', '8', 'nine', '9']


for line in line_list:
    for number in number_list1:
        length = len(line)
        index_start = 0
        i = 0
        while i < length:
            index = line.find(number, index_start)
            if index != -1:
                if not number.isdigit():
                    number1 = number_dict[number]
                    number_index[index] = number1
                else:
                    number_index[index] = number
            index_start += 1
            i += 1

    number_index_sorted = dict(sorted(number_index.items()))

    i = list(number_index_sorted.values())
    first_digit = i[0]
    last_digit = i[-1]
    total_string = first_digit + last_digit
    print(f'Het antwoord was {answer}, het is nu: first = {first_digit} + last = {last_digit}')
    answer += int(total_string)

    number_index.clear()
    number_index_sorted.clear()

print(answer)
