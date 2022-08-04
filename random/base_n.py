from operator import index, not_


base_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
base_n = input("enter base number")
base = []
for x in range(base_list[index(int(base_n))]):
    base.append(x)
print(base)


number = input("number")
in_base = []
not_base = 0
for i in range(int(number)):
    if i in base:
        in_base = int(i)
    else:
        not_base = not_base + 1
based_number = in_base + not_base
print(in_base)
