#Open the file and put each line in a listh
values = open("input1.txt", "r").readlines()
#values = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
#temp_list = [''] * len(values)

'''
first_digit = "A"
last_digit = "A"
total = 0
numbers = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
'''

'''
#Doesn't work as numbers must be replaced in chronological order, not from least to greatest

for i in range(len(values)):
    for j in range(len(numbers)):
        if numbers[j] in values[i]:
            print(values[i])
            values[i] = values[i].replace(numbers[j], digits[j])
print(values)
'''

'''

for i in range(len(values)):
    for j in range(len(values[i])):
        length = len(values[i])
        #print(length, values)
        try:
            if j < length - 2:
                if values[i][j] == "o" and values[i][j+1] == "n" and values[i][j+2] == "e":
                    values[i] = values[i].replace("one", "1")
                elif values[i][j] == "t" and values[i][j+1] == "w" and values[i][j+2] == "o":
                    values[i] = values[i].replace("two", "2")
                elif values[i][j] == "s" and values[i][j+1] == "i" and values[i][j+2] == "x":
                    values[i] = values[i].replace("six", "6")
            if j < length - 3:
                #print("if activated")
                if values[i][j] == "f" and values[i][j+1] == "o" and values[i][j+2] == "u" and values[i][j+3] == "r":
                    values[i] = values[i].replace("four", "4")
                elif values[i][j] == "f" and values[i][j+1] == "i" and values[i][j+2] == "v" and values[i][j+3] == "e":
                    #print("five activated")
                    values[i] = values[i].replace("five", "5")
                elif values[i][j] == "n" and values[i][j+1] == "i" and values[i][j+2] == "n" and values[i][j+3] == "e":
                    values[i] = values[i].replace("nine", "9")
            if j < length - 4:
                if values[i][j] == "t" and values[i][j+1] == "h" and values[i][j+2] == "r" and values[i][j+3] == "e" and values[i][j+4] == "e":
                    values[i] = values[i].replace("three", "3")
                elif values[i][j] == "s" and values[i][j+1] == "e" and values[i][j+2] == "v" and values[i][j+3] == "e" and values[i][j+4] == "n":
                    values[i] = values[i].replace("seven", "7")
                elif values[i][j] == "e" and values[i][j+1] == "i" and values[i][j+2] == "g" and values[i][j+3] == "h" and values[i][j+4] == "t":
                    values[i] = values[i].replace("eight", "8")
            #print(j, "end of try")
        except:
            pass
'''
        
#print(values)



'''
for i in values:
    for j in i:
        try:
            temp = int(j)
            if first_digit == "A":
                first_digit = j
            last_digit = j
        except:
            pass
    adding = int(first_digit + last_digit)
    print(adding)
    total += adding
    first_digit = "A"
print(total)
'''
#values.close()


#Internet solution after I couldn't figure it out
#https://gboeer.github.io/2023/12/01/advent-of-code-day-1-trebuchet-puzzle-solution.html
import re

def substring_idx(text, substring):
    """Return the starting indices of all occurrences of substring in text."""
    pattern = re.escape(substring)
    return [match.start() for match in re.finditer(pattern, text)]

def solve2():
    """Solve second part of the puzzle"""

    # produce a map for different string representations to ints (e.g. 'one': 1, '1': 1)
    str_digit_map = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    str_digit_map = {s: str(i) for i, s in enumerate(str_digit_map, start=1)}
    str_digit_map.update({str(i): str(i) for i in range(1, 10)})

    result = 0
    for line in values:
        # in each line find the starting indices for each number string
        findings = {}
        for s, v in str_digit_map.items():
            findings.update({i: v for i in substring_idx(line, s)})
        # the minimum and maximum indices correspond to the first and last digit in the string
        min_idx, max_idx = min(findings), max(findings)
        # concat digits and sum up
        result += int("".join((findings[min_idx], findings[max_idx])))

    return result
print(solve2())