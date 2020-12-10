import re

BOOKS_FILE = 'books.md'
BOOK_REGEX = r'''####\s+(?P<position>\d+)\.\s+\[(?P<book>.+?)\]\((?P<book_url>.+?)\)\s+by\s+(?P<author>[\w'-]+\s+[\w'-]+)\s+\((?P<recommended>\d{1,3}\.\d+%)\s+recommended\)\s+!\[.*?\]\((?P<cover_url>.+?)\)\s+\"(?P<description>.+?)\"\s+\[.*?\]\(.*?\)'''


def main():
    extract_all_books()


def extract_all_books():
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)

    with open(BOOKS_FILE) as f:
        for i, book in enumerate(book_pattern.finditer(f.read())):
            print(f'Книга {i}: {book}')


if __name__ == '__main__':
    main()
