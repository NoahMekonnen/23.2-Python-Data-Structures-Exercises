def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    tru_elements = []
    for i in range(len(lst)):
        if lst[i]:
            tru_elements.append(lst[i])

    return tru_elements

