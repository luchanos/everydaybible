from exceptions import WrongBorders, TooMuchLines
from settings import STRING_LIMIT
from utils import supress_errors


@supress_errors
def bible_parser(start=0, end=100):
    if end < start:
        raise WrongBorders("конечная строка не может быть меньше начальной!")
    if end - start > STRING_LIMIT:
        raise TooMuchLines("запрошен слишком большой промежуток строк! Лимит - {}!".format(STRING_LIMIT))
    with open(file='Bible.txt', mode='r', encoding='1251') as file:
        return ''.join(file.readlines()[start:end])
