class WrongBorders(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return "Wrong borders error, {}".format(self.message)
        else:
            return "Wrong borders error has been raised!"


class TooMuchLines(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return "Too Much Lines error, {}".format(self.message)
        else:
            return "Too Much Lines has been raised!"
