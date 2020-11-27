import os
import sys


if __name__ == '__main__':
    # /usr/local/bin/python3.6 3/print_arg.py
    script_path = sys.argv[0]
    script_name = os.path.basename(script_path)  # название файла
    script_dir = os.path.dirname(script_path)  # путь до скрипта

    print(script_name)
    print(script_dir)
    print(sys.argv[1:])
