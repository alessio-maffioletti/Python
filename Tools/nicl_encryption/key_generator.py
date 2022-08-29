import random

#define character to use
chars = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%$^&*()_+}{|"
#make character list
char_list = []
for char in chars:
    char_list.append(char)
#shuffle list
random.shuffle(char_list)
#print in user readable format
key = ""
for char in char_list:
    key += char
print(f"\"{key}\"")