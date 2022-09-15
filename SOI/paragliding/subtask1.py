def calc(placeNum, Positions, Hights, case):
    p = []
    final = ""
    class places:
        def __init__(self, pos, hight):
            self.pos = pos
            self.hight = hight

    for x in range(placeNum):
        p.append(places(Positions[x], Hights[x]))
        

    for x in range(placeNum):  
        for place in range(placeNum):
            
            if x != place:
                if p[x].hight > p[place].hight:
                    final += (f"{abs(int(p[x].pos) - int(p[place].pos))} ")
                else:
                    final += (f"0 ")

    print(f"Case #{case}: {final}")

with open('input.txt', 'r') as f:
    x = f.read()
raw_input = x.split()
repeats = 0
for x in range(0, int(raw_input[0])):
    case = x*5
    placeNum = int(raw_input[case+1])
    Positions = []
    Positions.append(int(raw_input[case+2]))
    Positions.append(int(raw_input[case+3]))
    Hights = []
    Hights.append(int(raw_input[case+4]))
    Hights.append(int(raw_input[case+5]))
    #print(placeNum, Positions, Hights)
    calc(placeNum, Positions, Hights, repeats)
    repeats += 1

