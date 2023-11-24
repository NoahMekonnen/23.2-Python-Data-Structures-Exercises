def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    dict_keys = d.keys()
    keys = []
    for key in dict_keys:
        keys.append(key)
    values = d.values()
    final_max_key = 0
    final_min_key = 0
    if type(keys[0]) == int or type(keys[0]) == float:
        max_key = 0
        min_key = 10000000000000000000000000
        for key in keys:
            if key > max_key:
                max_key = key
            if key < min_key:
                min_key = key
        final_max_key = max_key
        final_min_key = min_key
    elif type(keys[0]) == str:
        max_key = 'a'
        min_key = 'zzzzzzzzzz'
        for key in keys:
            if key > max_key:
                max_key = key
            if key < min_key:
                min_key = key
        final_max_key = max_key
        final_min_key = min_key
    return (final_min_key,final_max_key)
    
    
        