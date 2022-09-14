import sys
import argparse as arg

def encryption(message, key):
    keyIndex = 0
    final = ""
    for char in message:
        final += chr(ord(char) + (ord(key[keyIndex]) - ord("a")))
        if keyIndex + 1 >= len(key):
            keyIndex = 0
        else:
            keyIndex += 1
    print(final)

def decryption(message, key):
    keyIndex = 0
    final = ""
    for char in message:
        final += chr(ord("a") + (ord(char) - ord(key[keyIndex])))
        if keyIndex + 1 >= len(key):
            keyIndex = 0
        else:
            keyIndex += 1
    print(final)


def main():
    parser = arg.ArgumentParser()
    parser.add_argument('option', help='decrypt or encrypt')
    parser.add_argument('message', help='message to encrypt/decrypt')
    parser.add_argument('key', help='key for ecryption/decryption')
    args = parser.parse_args()

    if args.option == "decrypt":
        decryption(args.message, args.key)
    elif args.option == "encrypt":
        encryption(args.message, args.key)
    else:
        print("please provide valid option: encrypt or decrypt")
    
    
if __name__ == "__main__":
    sys.exit(main())





