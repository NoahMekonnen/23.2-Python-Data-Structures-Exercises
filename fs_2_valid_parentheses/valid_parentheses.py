def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    normal = True
    for i in range(len(parens)):
        if parens[:i].count('(') < parens[:i].count(')'):
            normal = False 

    if parens.count('(') == parens.count(')') and normal:
        return True
    return False

    