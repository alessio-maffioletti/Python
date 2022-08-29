cap = 10
print("number = int(input('number to check: '))")
print("if number == 0:")
print("    print('even')")
for i in range(1,cap,2):
    print(f"elif number == {i}:")
    print("    print('odd')")
    print(f"elif number == {i+1}:")
    print("    print('even')")