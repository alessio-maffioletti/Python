def calc(placeNum, Positions, Heights, repeats):

    class places:
        def __init__(self, pos, height):
            self.pos = pos
            self.height = height

    p = []
    final = ""
    for x in range(int(placeNum)):
        p.append(places(Positions[x], Heights[x]))

    for place in range(int(placeNum)):
        final += str(int(p[-1].pos) - int(p[place].pos)) + ' '
    
    print(f"Case #{repeats}: {final}")


with open('input.txt', 'r') as f:
    howmanyplaces = f.readline()

    for iter in range(0,int(howmanyplaces)):
        places = int(f.readline())
        position = f.readline().split()
        heights = f.readline().split()
        calc(places, position, heights, iter)
