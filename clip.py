import clipboard as cl
import sys

argument = sys.argv[1:2]
board = {

        }
with open('cliplist.txt', 'r') as r:
    for line in r:
        val = line.split(':')
        board[val[0]] = val[1]
r.close()

def store(name):
    cc = cl.paste()
    board[name] = cc.strip()
    print(board)

def load(x):
    if x in board:
        cl.copy(board[x])
    else:
        print('cant find ')
    
if argument == ['store']:
    store(input('name of clip: '))
elif argument == ['load']:
    print(board)
    load(input('what do you want to load? '))
else:
    print('invalid argument: \nYou can only use following arguments: store, load')

with open('cliplist.txt', 'w') as f:
    for i in board:
        f.write(i + ':' + board[i].strip() + '\n')
f.close()