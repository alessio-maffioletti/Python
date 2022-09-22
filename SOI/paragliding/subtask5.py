
def check_next_pos(list, index):
    highest = 0

    #takes current place and loops through remaining indexes in the list
    for next in range(1, len(list)-index):
        #checks if current places height is higher then the next places height
        if index+next <= len(list) and int(list[index].height) > int(list[index+next].height):
            #adds the diffrence of the two places to the variable "highest"
            highest = abs(int(list[index].pos) - int(list[index+next].pos))
        #breaks the loop if its not the case to avoid errors
        else:
            break

    
    return highest

def check_next_neg(list, index):
    highest = 0

    #takes current place and loops through remaining indexes in the list but with the step -1
    for next in range(index-1, -1, -1):
        #adds the diffrence of the two places to the variable "highest"
        if int(list[index].height) > int(list[next].height):
            #adds the diffrence of the two places to the variable "highest"
            highest = abs(int(list[index].pos) - int(list[next].pos))
        #breaks the loop if its not the case to avoid errors
        else:
            break
        
    return highest

def calc(place_num, positions, heights, repeats):
    class Places:
        def __init__(self, pos, height):
            self.pos = pos
            self.height = height


    p = []
    final = 0

    #Create object inside class "Places" for every place_num
    for x in range(int(place_num)):
        p.append(Places(positions[x], heights[x]))

    for place in range(place_num):
        #check next positive highest place with function "check_next_pos"
        next_neg = check_next_neg(p, place)
        #check next negative highest place with function "check_next_neg"
        next_pos = check_next_pos(p, place)

        #add higher value to the end result
        if next_neg > next_pos:
            final += int(next_neg)
        else:
            final += int(next_pos)
    #print end result
    print(f"Case #{repeats}: {final}")



with open('input.txt', 'r') as f:
    #read file with amount of repeats
    howmanyplaces = f.readline()

    #set variables to the values of the file and call function "calc" with the values as parameter
    for iter in range(0,int(howmanyplaces)):
        place_num = int(f.readline())
        position = f.readline().split()
        heights = f.readline().split()
        calc(place_num, position, heights, iter)