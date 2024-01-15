data = open('input.txt', 'r')

games = data.readlines()



def part_one():
    total = 0
    for i in range(len(games)):
        gameId = int(games[i].split(":")[0].strip(" Game"))
        #print(gameId)
        rounds = games[i].split(":")[1].strip(" \n").split("; ")
        possible = True
        for j in rounds:
            # Check if reds, greens, or blues surpass the max values
            # If they do, set possible to False
            temp_list = j.split(", ")
            for k in temp_list:
                if ('blue' in k and int(k.split(" ")[0]) > 14):
                    possible = False
                elif ('red' in k and int(k.split(" ")[0]) > 12):
                    possible = False
                elif ('green' in k and int(k.split(" ")[0]) > 13):
                    possible = False
            #print(temp_list)
            #if('blue' in )
            #pass
        if possible:
            total += gameId
    print(total)

def part_two():
    total = 0
    for i in range(len(games)):
        gameId = int(games[i].split(":")[0].strip(" Game"))
        #print(gameId)
        rounds = games[i].split(":")[1].strip(" \n").split("; ")
        red = 0
        blue = 0
        green = 0
        for j in rounds:
            # Check if reds, greens, or blues surpass the max values
            # If they do, set possible to False
            temp_list = j.split(", ")
            for k in temp_list:
                if ('blue' in k and int(k.split(" ")[0]) > blue):
                    blue = int(k.split(" ")[0])
                elif ('red' in k and int(k.split(" ")[0]) > red):
                    red = int(k.split(" ")[0])
                elif ('green' in k and int(k.split(" ")[0]) > green):
                    green = int(k.split(" ")[0])
            #print(temp_list)
            #if('blue' in )
            #pass
        total += (blue * green * red)
    print(total)
part_two()