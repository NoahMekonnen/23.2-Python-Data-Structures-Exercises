def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    str_num1 = str(num1)
    str_num2 = str(num2)
    count = 0
    for num in str_num1:
        if str_num1.count(num) == str_num2.count(num):
            count+=1
    return count == len(str_num1)

