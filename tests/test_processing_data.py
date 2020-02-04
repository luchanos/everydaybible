from tests.conftest import test_msg
from bible_bot_app.utils import full_name_getter
from bible_bot_app.bible_parser import load_bible


def test_load_bible():
    result = load_bible()
    assert result


def test_full_name_getter():
    result = full_name_getter(test_msg)
    assert result == 'Nikolas Luchanos'
