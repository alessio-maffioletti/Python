import sys
import argparse as arg

def main():
    parser = arg.ArgumentParser()
    parser.add_argument('msg', help = "message to encrypt", type=str)
    parser.add_argument('--key', help = "key for encryption")
    parser.add_argument('--keyfile', help = "keyfile for encryption")
    args = parser.parse_args()
    
    #make key a list
    key = []
    #check if the key is printed
    if args.key is not None:
        for char in args.key:
            key.append(char)
    #check if key is a file
    if args.keyfile is not None:
        with open(args.keyfile, 'r') as f:
            raw_key = f.read()
        for char in raw_key:
            key.append(char)

    #convert message to indexes
    index_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    indexes = []
    for char in args.msg:
        indexes.append(index_list.index(char))
    
    #convert indexes to encrypted message
    converted = ""
    for index in indexes:
        converted += key[index]
    print(f"\"{converted}\"")
    
if __name__ == "__main__":
    sys.exit(main())