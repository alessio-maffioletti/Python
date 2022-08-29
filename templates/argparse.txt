import sys
import argparse as arg

def main():
    parser = arg.ArgumentParser()
    parser.add_argument('--foo', action=arg.BooleanOptionalAction, help='foo help', default=False)
    parser.add_argument('nome', type=int)
    parser.add_argument('surname', type=int)
    args = parser.parse_args()
    print(args.nome)
    print(args.surname)
    print(args.foo)

    int(args.surname)
    

if __name__ == "__main__":
    sys.exit(main())