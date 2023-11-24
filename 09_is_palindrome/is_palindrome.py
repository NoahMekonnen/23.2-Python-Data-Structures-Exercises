def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    pali = True
    phrase_list = phrase.split()
    stripped_list = [char for char in phrase if char != ' ']
    for i in range(len(stripped_list)):
        stripped_list[i] = stripped_list[i].lower()
    for i in range(len(stripped_list)):
        if stripped_list[i] != stripped_list[len(stripped_list)-i-1]:
            pali = False
    return pali
