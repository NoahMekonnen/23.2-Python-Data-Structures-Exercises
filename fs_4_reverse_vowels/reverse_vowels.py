def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    string_list = [char for char in s]
    vowels_reversed = []
    for char in s:
        if 'aeiou'.count(char.lower()) == 1:
            vowels_reversed.insert(0, char)
    vowel_count = 0
    for i in range(len(string_list)):
        if 'aeiou'.count(string_list[i].lower()) == 1:
            string_list[i] = vowels_reversed[vowel_count]
            vowel_count += 1
    return ''.join(string_list)

        
