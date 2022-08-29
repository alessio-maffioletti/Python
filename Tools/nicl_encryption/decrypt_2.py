import sys
import argparse as arg

def main():
    parser = arg.ArgumentParser()
    parser.add_argument('msg', help="message to decrypt")
    parser.add_argument('key', help="key used in encryption")
    args = parser.parse_args()
    
    #make key a list
    key = []
    for char in args.key:
        key.append(char)

    #convert encrypted message to list of indexes of the key
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    final = ""
    for char in args.msg:
        #print(key.index(char))
    #convert indexes into decrypted message with alphabet
        final += alphabet[int(key.index(char))]
    print(final)

if __name__ == "__main__":
    sys.exit(main())