import argparse


def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.name_subparser == 'save':
        print('Вывод в файл')
    elif args.name_subparser == 'show':
        print('Вывод в консоль')


def create_save_subparser(subparsers):
    save_subparser = subparsers.add_parser('save')
    save_subparser.add_argument('-o', '--output_file',  # python3 3/count.py 5 5 save -o gvdfsgfd
                                required=True)


def create_show_subparser(subparsers):
    show_subparser = subparsers.add_parser('show')


def create_parser():
    parser = argparse.ArgumentParser()  # Основной парсер
    parser.add_argument('start')
    parser.add_argument('step')

    subparsers = parser.add_subparsers(dest='name_subparser', description='')
    create_save_subparser(subparsers)  # создание подпарсера save
    create_show_subparser(subparsers)  # создание подпарсера show

    parser.add_argument('-c', '--count',
                        default=5)

    return parser


if __name__ == '__main__':
    main()
