def square(x: int | float) -> int | float:
    """
    This function squares the given number.
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """
    This function exponentizes by himself
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    This function returns a function that
    keeps calling the given function with the given number
    """
    count = 0

    def inner() -> float:
        """
        This function calls the given function with
        given number and returns the result
        """
        nonlocal count
        if count == 0:
            count = function(x)
        else:
            count = function(count)
        return count
    return inner
