from typing import Callable


def decorator_template_no_params(func: Callable):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrapper
