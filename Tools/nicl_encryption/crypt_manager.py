import sys
import argparse as arg
import random

intro = """
                                                                  
 @@@@@@@ @@@@@@@  @@@ @@@ @@@@@@@  @@@@@@@                        
!@@      @@!  @@@ @@! !@@ @@!  @@@   @!!                          
!@!      @!@!!@!   !@!@!  @!@@!@!    @!!                          
:!!      !!: :!!    !!:   !!:        !!:                          
 :: :: :  :   : :   .:     :          :                           
                                                                  
                                                                  
@@@@@@@@@@   @@@@@@  @@@  @@@  @@@@@@   @@@@@@@  @@@@@@  @@@@@@@  
@@! @@! @@! @@!  @@@ @@!@!@@@ @@!  @@@ !@@           @@! @@!  @@@ 
@!! !!@ @!@ @!@!@!@! @!@@!!@! @!@!@!@! !@! @!@!@  @!!!:  @!@!!@!  
!!:     !!: !!:  !!! !!:  !!! !!:  !!! :!!   !!:     !!: !!: :!!  
 :      :    :   : : ::    :   :   : :  :: :: :  ::: ::   :   : : 
                                                                                      
Python encryption and decryption system.
    \"python3 crypt_manager.py --help\" to get started
"""

char_list = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!%$&\'\"()*+,-./:;<=>?@[\]^_{|}~ ")

class encrypt:
    def main(keyfile, msg):
        #make key a list
        key = []
        with open(keyfile, 'r') as f:
            raw_key = f.read()
        for char in raw_key:
            key.append(char)

        #convert message to indexes
        indexes = []
        for char in msg:
            indexes.append(char_list.index(char))
        
        #convert indexes to encrypted message
        converted = ""
        for index in indexes:
            converted += key[index]
        print(f"\'{converted}\'")

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
        final = ""
        for char in msg:
        #convert indexes into decrypted message with alphabet
            final += char_list[int(key.index(char))]
        print(final)

class generate:
    def main(output):
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