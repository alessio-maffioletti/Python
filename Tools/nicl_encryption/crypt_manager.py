import sys
import argparse as arg
import random

intro = """
                                                                                                                                                           
                                                                                                                                                           
                                                   ,d                                                                                                      
                                                   88                                                                                                      
 ,adPPYba,  8b,dPPYba,  8b       d8  8b,dPPYba,  MM88MMM     88,dPYba,,adPYba,   ,adPPYYba,  8b,dPPYba,   ,adPPYYba,   ,adPPYb,d8   ,adPPYba,  8b,dPPYba,  
a8"     ""  88P'   "Y8  `8b     d8'  88P'    "8a   88        88P'   "88"    "8a  ""     `Y8  88P'   `"8a  ""     `Y8  a8"    `Y88  a8P_____88  88P'   "Y8  
8b          88           `8b   d8'   88       d8   88        88      88      88  ,adPPPPP88  88       88  ,adPPPPP88  8b       88  8PP"""""""  88          
"8a,   ,aa  88            `8b,d8'    88b,   ,a8"   88,       88      88      88  88,    ,88  88       88  88,    ,88  "8a,   ,d88  "8b,   ,aa  88          
 `"Ybbd8"'  88              Y88'     88`YbbdP"'    "Y888     88      88      88  `"8bbdP"Y8  88       88  `"8bbdP"Y8   `"YbbdP"Y8   `"Ybbd8"'  88          
                            d8'      88                                                                                aa,    ,88                          
                           d8'       88                                                                                 "Y8bbdP"                           
Python encryption and decryption system.
    \"python3 crypt_manager.py --help\" to get started
"""

class encrypt:
    def main(keyfile, msg):
        #make key a list
        key = []
        with open(keyfile, 'r') as f:
            raw_key = f.read()
        for char in raw_key:
            key.append(char)

        #convert message to indexes
        index_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
        indexes = []
        for char in msg:
            indexes.append(index_list.index(char))
        
        #convert indexes to encrypted message
        converted = ""
        for index in indexes:
            converted += key[index]
        print(f"\"{converted}\"")

class decrypt:
    def main(keyfile, msg):
        #make key a list
        key = []
        if keyfile is not None:
            with open(keyfile, 'r') as f:
                raw_key = f.read()
            for char in raw_key:
                key.append(char)

        #convert encrypted message to list of indexes of the key
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
        final = ""
        for char in msg:
        #convert indexes into decrypted message with alphabet
            final += alphabet[int(key.index(char))]
        print(final)

class generate:
    def main(output):
        #define character to use
        chars = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+}{:?><=[]|;/.,"
        
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
        
        #output key into file
        
        if output is not None:
            with open(f'{output}', 'w+') as f:
                f.write(key)
        else:
            print(f"\"{key}\"")

def error(type):
    #print the not provided argument and exit
    print(f"please provide {type} argument")
    exit()

def main():
    if len(sys.argv)==1:
        print(intro)
    parser = arg.ArgumentParser()
    parser.add_argument('option', help="option to use: generate, encrypt, decrypt")
    parser.add_argument('--message', help="message to encrypt/decrypt")
    parser.add_argument('--keyfile', help="keyfile used in encryption and decryption")
    parser.add_argument('--output', help="output file used in generation")
    args = parser.parse_args()
    #call encrypt option and pass given arguments
    if args.option == "encrypt":
        #check if necessary arguments were provided and call error func. if not
        assert args.message != None, error("message")
        assert args.keyfile != None, error("keyfile")
        encrypt.main(args.keyfile, args.message)
    #call decrypt options and pass arguments
    elif args.option == "decrypt":
        #check if necessary arguments were provided and call error func. if not
        assert args.message != None, error("message")
        assert args.keyfile != None, error("keyfile")
        decrypt.main(args.keyfile, args.message)
    #call generate options arguments
    elif args.option == "generate":
        #check if necessary arguments were provided and call error func. if not
        assert args.output != None, error("output")
        generate.main(args.output)
    else:
        print("enter valid option: generate, encrypt, decrypt")

if __name__ == "__main__":
    sys.exit(main())