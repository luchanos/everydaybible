def bible_parser(start, end):
    with open(file='Bible.txt', mode='r', encoding='1251') as file:
        return ''.join(file.readlines()[start:end])
