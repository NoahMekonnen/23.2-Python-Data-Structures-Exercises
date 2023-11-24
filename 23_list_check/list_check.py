def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    all_list = True
    for thing in lst:
        if type(thing) != list:
            all_list = False
    return all_list
