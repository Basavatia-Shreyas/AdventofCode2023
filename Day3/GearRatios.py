import re
import numpy as np
import pandas as pd

data = open('input.txt', 'r').readlines()
for i in range(len(data)):
    data[i] = data[i].strip("\n")
    data[i] += " "

symbols = "!@#$%^&*()+=_-/<>[]\|:;`~,?{}"

def part_one():
    total = 0
    for i in range(len(data)):
        result = list(re.finditer(r'\d+', data[i]))
        #print(type(list(result)[0].span()[1]))

        for j in range(len(result)):
            found_symbol = False
            right_index = result[j].span()[1]
            if result[j].span()[1] == len(data[i]):
                right_index = result[j].span()[1] - 1
            
            left_index = result[j].span()[0]-1
            if result[j].span()[0] == 0:
                left_index = result[j].span()[0]
            #print(num, num2)
            #Check to the right
            #right_index = result[j].span()[1] + num
            if data[i][right_index] in symbols:
                found_symbol = True
            #Check to the left
            #left_index = result[j].span()[0]
            if data[i][left_index] in symbols:
                found_symbol = True
            
            #Check above
            if i - 1 >= 0:
                for k in data[i-1][left_index: right_index + 1]:
                    if k in symbols:
                        found_symbol = True
            #Check below
            if i + 1 < len(data):
                for k in data[i+1][left_index : right_index + 1]:
                    if k in symbols:
                        found_symbol = True
            
            #print(result[j].span())
            if found_symbol == True:
                total += int(result[j].group())
                print(total, result[j].group())
        
    return total
#print(part_one())


numbers = '1234567890'

def part_two():
    total = 0
    max_index = 139
    # For each line
    for i in range(len(data)):
        #print(len(data[i]), data[i][139])
        
        # Find the * in each line
        result = list(re.finditer(r'[*]', data[i]))
        for j in range(len(result)):
            # For each *, check for 2 adjacent part numbers
            part_numbers = []
            #Check left
            temp = ''
            counter = result[j].span()[0] - 1
            while data[i][counter] in numbers and counter >= 0:
                temp += data[i][counter]
                counter -= 1
            if temp != "":
                part_numbers.append(temp[::-1])

            #Check right
            temp = ''
            counter = result[j].span()[1]
            while data[i][counter] in numbers and counter <= max_index:
                temp += data[i][counter]
                counter += 1
            if temp != "":
                part_numbers.append(temp)

            #Check above
            method_one = False
            above_index = result[j].span()[0]
            if data[i-1][above_index] in numbers:
                temp = data[i-1][above_index]
                counter = result[j].span()[1]
                while data[i-1][counter] in numbers and counter <= max_index:
                    temp += data[i-1][counter]
                    counter += 1
                counter = result[j].span()[0]-1
                while data[i-1][counter] in numbers and counter >= 0:
                    temp = data[i-1][counter] + temp
                    counter -= 1
                if temp != "":
                    part_numbers.append(temp)
                    method_one = True
            
            if data[i-1][above_index + 1] in numbers and not method_one:
                temp = data[i-1][above_index + 1]
                counter = result[j].span()[1] + 1
                while data[i-1][counter] in numbers and counter <= max_index:
                    temp += data[i-1][counter]
                    counter += 1
                if temp != "":
                    part_numbers.append(temp)

            if data[i-1][above_index - 1] in numbers and not method_one:
                temp = data[i-1][above_index - 1]
                counter = result[j].span()[0] - 2
                while data[i-1][counter] in numbers and counter >= 0:
                    temp = data[i-1][counter] + temp
                    counter -= 1
                if temp != "":
                    part_numbers.append(temp)

            #Check below
            method_one = False
            below_index = result[j].span()[0]
            if data[i+1][below_index] in numbers:
                temp = data[i+1][below_index]
                counter = result[j].span()[1]
                while data[i+1][counter] in numbers and counter <= max_index:
                    temp += data[i+1][counter]
                    counter += 1
                counter = result[j].span()[0]-1
                while data[i+1][counter] in numbers and counter >= 0:
                    temp = data[i+1][counter] + temp
                    counter -= 1
                if temp != "":
                    part_numbers.append(temp)
                    method_one = True
            
            if data[i+1][below_index + 1] in numbers and not method_one:
                temp = data[i+1][below_index + 1]
                counter = result[j].span()[1] + 1
                while data[i+1][counter] in numbers and counter <= max_index:
                    temp += data[i+1][counter]
                    counter += 1
                if temp != "":
                    part_numbers.append(temp)

            if data[i+1][below_index - 1] in numbers and not method_one:
                temp = data[i+1][below_index - 1]
                counter = result[j].span()[0] - 2
                while data[i+1][counter] in numbers and counter >= 0:
                    temp = data[i+1][counter] + temp
                    counter -= 1
                if temp != "":
                    part_numbers.append(temp)
            
            print(part_numbers)
            if len(part_numbers) == 2:
                total += (int(part_numbers[0]) * int(part_numbers[1]))
    return total
    

print(part_two())
