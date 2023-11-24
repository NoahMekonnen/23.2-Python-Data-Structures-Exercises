def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letters = []
    final_letter_count ={}

    for char in phrase:
        if char not in letters:
            letters.append(char)
            final_letter_count[char] = 1
        else:
            final_letter_count[char] += 1
    return final_letter_count
         
        

