seed = [629551616, 310303897, 265998072, 58091853, 3217788227, 563748665, 2286940694, 820803307, 1966060902, 108698829, 190045874, 3206262, 4045963015, 223661537, 1544688274, 293696584, 1038807941, 31756878, 1224711373, 133647424]
import re
#Format of input
'''
seed - soil
destination source range
destination source range
...

soil - fertilizer
destination source range
...

'''

file = open('input.txt', 'r')
almanac = file.read()
#almanac = almanac.split('\n\n')
#print(almanac[1])

with open('input.txt', 'r') as f:
    puzzle_input = f.read()

'''
for i in range(len(almanac)):
    almanac[i] = almanac[i].split('\n')[1:]
    for j in range(len(almanac[i])):
        almanac[i][j] = almanac[i][j]
'''

def part_one(seeds):
    # Iterate through each seed
    for i in range(len(seeds)):
        # Iterate through each section of the map
        for j in range(len(almanac)):
            # Iterate through each line in the section
            for k in range(len(almanac[j])):
                temp = almanac[j][k].split(" ")
                destination = int(temp[0])
                source = int(temp[1])
                length = int(temp[2])
                #print(seeds[i], destination, source, length)
                # Check if the seed is in the source length
                if (seeds[i] >= source and seeds[i] <= source + length - 1):
                    # If so, apply the transformation by using the difference between source and destination
                    difference = source - destination
                    #print(seeds[i], seeds[i] - difference, destination, source, difference, length)
                    seeds[i] -= difference
                    break
    return seeds
                    
def part2(puzzle_input):
    segments = puzzle_input.split('\n\n')
    intervals = []

    for seed in re.findall(r'(\d+) (\d+)', segments[0]):
        x1, dx = map(int, seed)
        x2 = x1 + dx
        intervals.append((x1, x2, 1))

    min_location = float('inf')
    while intervals:
        x1, x2, level = intervals.pop()
        if level == 8:
            min_location = min(x1, min_location)
            continue

        for conversion in re.findall(r'(\d+) (\d+) (\d+)', segments[level]):
            z, y1, dy = map(int, conversion)
            y2 = y1 + dy
            diff = z - y1
            if x2 <= y1 or y2 <= x1:    # no overlap
                continue
            if x1 < y1:                 # split original interval at y1
                intervals.append((x1, y1, level))
                x1 = y1
            if y2 < x2:                 # split original interval at y2
                intervals.append((y2, x2, level))
                x2 = y2
            intervals.append((x1 + diff, x2 + diff, level + 1)) # perfect overlap -> make conversion and let pass to next nevel 
            break

        else:
            intervals.append((x1, x2, level + 1))
  
    return min_location



#output = part_one(seed)
#print(min(output))
output = part2(puzzle_input)
print(output)

