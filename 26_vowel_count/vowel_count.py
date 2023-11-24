def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    final_vowel_count ={}
    letters = []
    for char in phrase.lower():
        if char not in letters and 'aeiou'.count(char) == 1:
            letters.append(char)
            final_vowel_count[char] = 1 
        elif char in letters and char != '?' and char != ' ' and 'aeiou'.count(char) == 1 and phrase.lower().count(char) > 1:
            final_vowel_count[char] += 1
    return final_vowel_count