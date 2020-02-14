from utils import supress_errors


@supress_errors
def func_with_error(*args, **kwargs):
    1 / 0


def test_supress_error():
    func_with_error()
