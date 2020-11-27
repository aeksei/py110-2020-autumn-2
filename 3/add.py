import argparse


def main():
    parser = create_parser()
    args = parser.parse_args()

    print(args.a + args.b)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('a',
                        type=int,
                        help='Первое число для сложения')
    parser.add_argument('b',
                        type=int,
                        help='Второе число для сложения')

    return parser


if __name__ == '__main__':
    main()
