from os import abort


def printErr(err, level=0):
    """Error logging function and aborts the program for level > 2

    :param err: An error or a string
    :type err: BaseException or str
    :param level: Level of error, defaults to 0
    :type level: int, optional
    """
    if level <= 1:
        level_str = 'NOTE: '
    elif level == 2:
        level_str = 'WARN: '
    elif level > 2:
        level_str = 'FATAL: '

    print(f'VolDist: {level_str}{err}')
    if level > 2:
        abort()
