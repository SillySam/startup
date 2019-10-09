import platform
from startup import operating_systems


def add(script_location):
    if platform.system() == 'Windows':
        operating_systems.Windows().add(script_location)
    else:
        raise OSError('This operating system is not supported')
