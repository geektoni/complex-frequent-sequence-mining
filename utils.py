import time


def timing(f):
    """
    Decorator to compute the performance of a function
    :param f: function
    :return: wrapped function
    """
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2-time1)*1000.0))

        return (time2-time1)*1000.0, ret
    return wrap
