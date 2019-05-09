

def hello_world():
    return 'hello world'


def create_num_list(length):
    return [x for x in range(length)]


def custom_func_x(x, const, power):
    """Return const * (x) ** power

    >>> custom_func_x(2,3,4)
    48
    >>> custom_func_x(3,1,4)
    81

    """
    return const * (x) ** power


def custom_non_lin_num_list(length, const, power):
    return [custom_func_x(x, const, power) for x in range(length)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()



