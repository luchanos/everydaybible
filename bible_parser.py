def bible_parser(start, end):
    with open(file='Bible.txt', mode='r', encoding='1251') as file:
        final = ''
        for x in range(10):
            a = file.readline()
            final += a
        return final
