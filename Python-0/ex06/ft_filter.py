def ft_filter(function, iterator):
    """
    filter.__doc__
    Return an iterator yielding those items of
    iterable for which function(item)
    is true. If function is None,
    return the items that are true.

    if function is none, the function lists
    the elements that evaluate to true
    that means function equals bool.
    else if every elemnst in list is true,
    return an iterator.
    """
    if function is None:
        function = bool

    for i in iterator:
        if function(i):
            yield i
