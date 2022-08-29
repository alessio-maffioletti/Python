import sys
import argparse as arg

def main():
    parser = arg.ArgumentParser()
    parser.add_argument('msg', help='Message to encrypt in quotes')
    args = parser.parse_args()
    raw_message = args.msg
    message = []
    raw_encryption_list = "abcdefghijklmnopqrstuvwxyz"
    encryption_list = []
    for x in raw_encryption_list:
        encryption_list.append(x)
    final = ""
    for char in raw_message:
        message.append(char)
    final += str(encryption_list.index(message[2]))
    for index in range(1, len(message)):
        if message[index] == " ":
            final += str(",") + " "
        else:
            final += str(",") + str(encryption_list.index(message[index])+2)
    print(f"\"{final}\"")

if __name__ == "__main__":
    sys.exit(main())