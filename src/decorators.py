from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    @log()
    def my_function(x, y):

    return x + y


    print(my_function(1, 2))
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: ({args}, {kwargs})")
                else:
                    print(f"{func.__name__} error: {e}. Inputs: ({args}, {kwargs})")
                raise e

        return wrapper

    return decorator

# Для проверки работы Pytest
# @log()
# def my_function(x, y):
#
#     return x + y
#
#
# print(my_function(1, 2))
