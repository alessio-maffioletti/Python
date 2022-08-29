import sys
import argparse as arg

def main():
    parser = arg.ArgumentParser()
    parser.add_argument('msg', help='message to decrypt in strings', type=str)
    args = parser.parse_args()
    raw_char_list = "abcdefghijklmnopqrstuvwxyz"
    char_list = []
    raw_message = args.msg
    message = str(raw_message).split(",")
    final = ""
    
    #generate decode list
    for x in raw_char_list:
        char_list.append(x)
    
    #assign character to number
    for num in message:
        if num == " ":
            final += " "
        else:
            final += char_list[int(num)-2]
    
    print(final)


if __name__ == "__main__":
    sys.exit(main())