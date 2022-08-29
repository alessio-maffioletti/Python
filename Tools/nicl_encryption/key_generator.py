import random
import sys
import argparse as arg

def main():
    parser = arg.ArgumentParser()
    parser.add_argument('--output', help="output key to file")
    args = parser.parse_args()
    #define character to use
    chars = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%$^&*()_+}{|"
    
    #make character list
    char_list = []
    for char in chars:
        char_list.append(char)
    
    #shuffle list
    random.shuffle(char_list)
    
    #make in user readable format
    key = ""
    for char in char_list:
        key += char
    
    #output key into file or terminal
    
    if args.output is not None:
        with open(f'{args.output}', 'w+') as f:
            f.write(key)
    else:
        print(f"\"{key}\"")

if __name__ == "__main__":
    sys.exit(main())