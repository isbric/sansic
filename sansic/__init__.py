# -*- coding: utf-8 -*-


"""sansic.__init__: """

class Codes:
    def __init__(self):
        self.ENDC        = '\033[0m'
        self.INTENSE     = '\033[1m'
        self.ITALIC      = '\033[3m'
        self.UNDERLINE   = '\033[4m'
        self.BLACK       = '\033[30m'
        self.RED         = '\033[31m'
        self.GREEN       = '\033[32m'
        self.YELLOW      = '\033[33m'
        self.BLUE        = '\033[34m'
        self.MAGENTA     = '\033[35m'
        self.CYAN        = '\033[36m'
        self.WHITE       = '\033[37m'

    def disable(self):
        for var in [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]:
            setattr(self, var, '')

codes = Codes()
