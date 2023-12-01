
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

for line in line_list:
    fline_list = []
    for char in line:
        if char.isdigit():
            fline_list.append(char)
    fline_list_list.append(fline_list)

for flist in fline_list_list:
    first_digit = flist[0]
    last_digit = flist[-1]
    total_string = first_digit + last_digit
    answer += int(total_string)

print(answer)
