def ft_filter(function, iterator):
    if function is None:
        # function = bool
        function = bool
        
    for i in iterator:
        if function(i):
            yield i