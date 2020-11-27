import argparse


def main():
    parser = create_parser()
    args = parser.parse_args()

    count = 0
    for _ in args.file:
        count += 1

    print(count)


def create_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('file',
                        type=argparse.FileType('r'),
                        help='Путь до файла')

    return parser


if __name__ == '__main__':
    main()
