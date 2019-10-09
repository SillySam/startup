import sys


class StartupTemplate(object):

    def __init__(self, options=None):
        if type(self) is StartupTemplate:
            raise Exception('Cannot instantiate this class directly')
        self.python_location = sys.executable

    def add(self):
        # TODO: Don't allow invalid file names (security vulnerability)
        raise NotImplementedError('subclasses must override add()!')
