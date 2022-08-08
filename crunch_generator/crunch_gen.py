command = 'crunch 1 1 -p man me you hehs heh'
list = command.split()
a = ''
param = ''
for i in range(list.index('-p'),(len(list)-(list.index('-p')-list.index('-p')))):
    param = param + list[i] + ' '
for i in range(1,(len(list)-(list.index('-p')))):
    a = a + 'a'
    print(f'crunch {i} {i} -t {a} -o wlist{i}.txt {param}')
print('cat wlist1.txt wlist2.txt wlist3.txt > wlist4.txt')
