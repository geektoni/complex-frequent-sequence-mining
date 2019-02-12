import time

from pymining import itemmining


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


def count_occurences(res, length):
    count = [0 for x in range(0, length)]
    for e in res:
        count[len(e)-1] += 1
    return count

@timing
def frequent_itemset(input, min_supp):
    return itemmining.relim(input, min_supp)


