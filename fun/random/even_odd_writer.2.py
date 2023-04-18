cap = 1000
with open('even_odd.py', 'w+') as f:
    f.write("number = int(input('number to check: ')) \n")
    f.write("if number == 0:\n")
    f.write("    print('even')\n")
    for i in range(1,cap):
        f.write(f"elif number == {i}:\n")
        if (i%2 == 0):
            f.write("    print('even')\n")
        else:
            #f.write(f"elif number == {i+1}:\n")
            f.write("    print('odd')\n")
            #make a for loop