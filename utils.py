def supress_errors(func):
    """Декоратор для подавления ошибок"""
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as err:
            print(err)
    return wrapper
