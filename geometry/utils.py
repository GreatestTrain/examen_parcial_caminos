import numpy as np

def vectorize(n_arguments: int):
    def inner(func):
        def inner_2(arr, *args, **kwargs):
            assert arr.shape[1] == n_arguments
            return np.apply_along_axis(func, 1, arr, *args, **kwargs)
        inner_2.__doc__ = "[Vectorized] {}".format(func.__doc__)
        inner_2.__name__ = func.__name__ + "_st"
        return inner_2
    return inner