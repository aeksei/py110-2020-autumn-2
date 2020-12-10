import re
import ipaddress


IP4_PATTERN = re.compile(r'(?:(?:25[0-5]|2[0-4][0-9]|(?:1[0-9]|[1-9])?[0-9])\.){3}'
                         r'(?:25[0-5]|2[0-4][0-9]|(?:1[0-9]|[1-9])?[0-9])')

# r'25[0-5]'  # 250 - 255
# r'2[0-4][0-9]'  # 200 - 249
# r'1[0-9][0-9]'  # 100 - 199
#  r'[1-9][0-9]'  #  10 -  99
#       r'[0-9]'  #   0 -   9



def test_correct_ip():
    ip_list = [
        '8.8.8.8',
        '192.168.0.1',
        '10.0.0.1',
        '234.1.23.255',
        '123.123.123.123'
    ]

    for ip in ip_list:
        print(IP4_PATTERN.fullmatch(ip))
        print(ipaddress.ip_address(ip))


def test_incorrect_ip():
    ip_list = [
        '8,8.8.8',
        '1924.168.0.1',
        '10.345.0.1',
        '234.1.23.2558',
        '123.123.123!123',
        '1.01.001.0'
    ]

    for ip in ip_list:
        print(IP4_PATTERN.fullmatch(ip))
        print(ipaddress.ip_address(ip))


def task_1():
    word_list = [
        ',./ sdfsdf',
        'Ddfsdf',
        '@@##,sdfsdf',
        '123_sdfsdf',
        '123sdfsdf',
        ', s,dfsdf',
        '123, fewfew',
    ]

    word_pattern = re.compile(r'\w+')

    for word in word_list:
        print(word_pattern.search(word).group())


def task_2():
    word_list = [
        ',./ sdfsdf',
        'Ddfsdf',
        '@@##,sdfsdf',
        '123_sdfsdf',
        '123sdfsdf',
        ', s,dfsdf',
        '123, fewfew',
    ]

    two_char = re.compile(r'\b\w\w')

    for word in word_list:
        print(two_char.findall(word))


def task_3():
    emails = 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz'

    email_pattern = re.compile(r'@(\w+).(?:\w+)')
    # (a|b|c) -> [abc]
    print(email_pattern.findall(emails))


def task_4():
    date_str = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'

    date_regex = r'(?:\d\d)-(?:\d\d)-(?P<year>\d\d\d\d)'
    for date in re.finditer(date_regex, date_str):
        ...

    date_pattern = re.compile(date_regex)
    for date in date_pattern.finditer(date_str):
        print(date)
        print(date.groupdict())
        print(date['year'])
        print('------')


def main():
    # test_correct_ip()
    # test_incorrect_ip()
    # task_1()
    # task_2()
    # task_3()
    task_4()


if __name__ == '__main__':
    main()
