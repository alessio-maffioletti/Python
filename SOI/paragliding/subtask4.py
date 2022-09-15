from traceback import print_list


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
        print("new_place")
        diff_pos = 0
        diff_neg = 0
        
        for it in range(place, place_num):
            if place != it:
                if int(p[place].height) > int(p[it].height):
                    diff_pos = int(p[it].pos) - int(p[place].pos)
        #print(diff_pos)
        
        for it in range(place, place_num):
            if place != it:
                if int(p[place].height) > int(p[-it].height):
                    print(p[-it].height)
        #print(diff_neg)


                

    
    #print(f"Case #{repeats}: {final}")


with open('input.txt', 'r') as f:
    howmanyplaces = f.readline()

    for iter in range(0,int(howmanyplaces)):
        place_num = int(f.readline())
        position = f.readline().split()
        heights = f.readline().split()
        #print(place_num, position, heights)
        calc(place_num, position, heights, iter)