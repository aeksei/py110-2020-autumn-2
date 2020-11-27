FILENAME = 'test.txt'


def create_file(filename):
    with open(filename, 'a', encoding='utf-8') as f:
        while True:
            input_str = input('Введите строку: ')
            f.write(input_str)
            f.write('\n')
            f.flush()


def read_text_file(filename):
    with open(filename, 'r', encoding='utf-8') as f_read:
        for line in f_read:
            print(line, end='')


def read_bin_file(filename):
    with open(filename, 'rb') as f_bin:
        print(f_bin.read())


def text_to_bin(filename):
    with open(filename, 'rb') as f_src:  # откуда
        output_filename = 'output_' + filename  # название для выходного файла
        with open(output_filename, 'wb') as f_dst:  # куда
            for line in f_src:
                f_dst.write(line)
                f_dst.flush()


if __name__ == '__main__':
    # create_file(FILENAME)
    # read_text_file(FILENAME)
    # read_bin_file(FILENAME)
    text_to_bin(FILENAME)
