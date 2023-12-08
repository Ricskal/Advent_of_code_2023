# --- Day 1: Trebuchet?! ---
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
