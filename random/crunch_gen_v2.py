import os
import argparse as arg

parser = arg.ArgumentParser()
parser.add_argument('words', help='list of words inside parentheses', type = str)
parser.add_argument('--extra', type = str, help = 'all the extra arguments instide parentheses excluding -p, -t and -o')
args = parser.parse_args()
list_words = args.words.split()
pattern = ''
wordlist_amount = ''

for word in range(1,len(list_words)+1):
    pattern = pattern + 'a'
    command = f'crunch {word} {word} {args.extra} -o temporary_wordlist{word}.txt -t {pattern} -p {args.words}'
    wordlist_amount = wordlist_amount + f'temporary_wordlist{word}.txt '
    os.system(command)
os.system(f'cat {wordlist_amount} > tmp.txt')
os.system('uniq tmp.txt > wordlist.txt')
os.system('rm temporary_wordlist* | rm tmp.txt')