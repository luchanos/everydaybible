from logging import getLogger


logger = getLogger(__name__)


def supress_errors(func):
    """Декоратор для подавления ошибок"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            logger.error(err)
    return wrapper


def full_name_getter(message):
    name = message.from_user.first_name
    surname = message.from_user.last_name
    if not name:
        name = ''
    if not surname:
        surname = ''
    return f"{name} {surname}"
