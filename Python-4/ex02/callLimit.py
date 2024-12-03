def callLimit(limit: int):
    """
    A decorator factory that creates a decorator to
    limit the number of times a function can be called.

    This function returns a decorator (`callLimiter`)
    which can be applied to any function. The decorated
    function will track how many times it has been called
    and restrict further calls once the limit is exceeded.

    Parameters:
    limit (int): The maximum number of times the decorated
    function is allowed to be called.

    Returns:
    Callable: A decorator function (`callLimiter`) that
    limits the calls to the target function.
    """
    count = 0

    def callLimiter(function):
        """
        A decorator that wraps given function and limits its number of calls

        This decorator checks if the function
        has been called less than the specified limit. If so, it
        executes the function and increments the call counter.
        If the limit is exceeded, it prints an error
        message and does not execute the function.

        Parameters:
        function (Callable): The function to be wrapped and limited.

        Returns:
        Callable: A wrapper function that enforces the call limit.
        """

        def limit_function(*args: any, **kwds: any):
            """
            The inner function that limits the number of times
            the decorated function can be called.

            This function is executed each time the decorated function
            is called. It checks if the count of previous calls is
            less than the specified `limit`. If it is, the function is
            executed and the counter is incremented. If count exceeds limit,
            an error message is printed and the function is not executed.

            Parameters:
            *args: Positional arguments passed to the decorated function.
            **kwds: Keyword arguments passed to the decorated function.

            Returns:
            Any: The result of the decorated function if limit is not exceeded,
            or `None` if the limit is exceeded.
            """

            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
