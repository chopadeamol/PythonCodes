def sum(values):
    if not isinstance(values, (list, tuple)):        #original statement from book:-> if not isinstance(values, collections.iterable):
        raise TypeError("Paramter must be an interable type")
    total = 0
    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError("Element must be numeric")
        total = total + v
    return total

