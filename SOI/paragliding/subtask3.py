
def check_next_pos(list, index):
    highest = 0

    for next in range(1, len(list)-index):
        if index+next <= len(list) and int(list[index].height) > int(list[index+next].height):
            highest = abs(int(list[index].pos) - int(list[index+next].pos))
        else:
            break

    
    return highest

def check_next_neg(list, index):
    highest = 0

    for next in range(index-1, -1, -1):
        #print(f"debug:{int(list[index].height)}, {int(list[next].height)}")
        if int(list[index].height) > int(list[next].height):
            highest = abs(int(list[index].pos) - int(list[next].pos))
        else:
            break
        
    return highest

def calc(place_num, positions, heights, repeats):
    class Places:
        def __init__(self, pos, height):
            self.pos = pos
            self.height = height


    p = []
    final = ""
    for x in range(int(place_num)):
        p.append(Places(positions[x], heights[x]))

    for place in range(place_num):

        next_neg = check_next_neg(p, place)
        next_pos = check_next_pos(p, place)

        if next_neg > next_pos:
            final += str(next_neg) + ' '
        else:
            final += str(next_pos) + ' '
    print(f"Case #{repeats}: {final}")



with open('input.txt', 'r') as f:
    howmanyplaces = f.readline()

    for iter in range(0,int(howmanyplaces)):
        place_num = int(f.readline())
        position = f.readline().split()
        heights = f.readline().split()
        #print(place_num, position, heights)
        calc(place_num, position, heights, iter)