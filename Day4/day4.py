import re

data = open("input.txt", "r").readlines()

fixed = []
for i in range(len(data)):
    temp = data[i].split(":")[1].split("|")
    fixed.append([re.findall(r'\d+', temp[0]), re.findall(r'\d+', temp[1])])

winning = [41, 48, 83, 86, 17]
my_nums = [83, 86,  6, 31, 17,  9, 48, 53]

def part_one():
    total = 0
    # Iterate through the cards
    for i in fixed:
        counter = 0
        # Find all the matches with my numbers and winning numbers
        for j in i[1]:
            if j in i[0]:
                counter += 1
        # Add the correct score based on matches to the running total
        if counter >= 1:
            total += (2 ** (counter -1))
    return total

#print(part_one())

copies = {}
for i in range(212):
    copies[i] = 1

def part_two():
    total = 0
    #Iterate through the cards
    for i in range(len(fixed)):
        counter = 0
        # Find the number of matches with my numbers and the winning numbers
        for j in fixed[i][1]:
            if j in fixed[i][0]:
                counter += 1
        # Add to the number of instances of each card depending on the number of copies of the current card
        for j in range(i+1,i + counter+1):
            copies[j] += (copies[i])
    # Total all the instances
    for i in copies.values():
        total += i
    #print(copies)
    return total
print(part_two())
    