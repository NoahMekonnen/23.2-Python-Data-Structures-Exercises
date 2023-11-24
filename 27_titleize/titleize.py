def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    temp_list = phrase.split(" ")
    final_temp_list = []
    for i in range(len(temp_list)):
        temp_list[i] = temp_list[i].lower()
    for i in range(len(temp_list)):
        final_temp_list.append([char for char in temp_list[i]])
    for i in range(len(final_temp_list)):
        final_temp_list[i][0] = final_temp_list[i][0].upper()
        if i < len(final_temp_list)-1:
            final_temp_list[i].append(' ')
        final_temp_list[i] = ''.join(final_temp_list[i])
    return ''.join(final_temp_list)
