from bible_bot_app.exceptions import WrongBorders, TooMuchLines
from bible_bot_app.settings import STRING_LIMIT
from bible_bot_app.utils import supress_errors


def load_bible():
    with open(file='Bible.txt', mode='r', encoding='1251') as bible:
        return bible.readlines()


loaded_bible = load_bible()


@supress_errors
def bible_parser(start, end):
    if end < start:
        raise WrongBorders("конечная строка не может быть меньше начальной!")
    if end - start > STRING_LIMIT:
        raise TooMuchLines("запрошен слишком большой промежуток строк! Лимит - {}!".format(STRING_LIMIT))
    return ''.join(load_bible()[start:end])


@supress_errors
def parse_args(s: str):
    return s.split(' ')[1:]
