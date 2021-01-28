#!/usr/bin/python3


def is_Palindrome(word):
    '''
    Returns if a string is a palindrome.
    >>> is_Palindrome('a')
    True
    >>> is_Palindrome('yes')
    False
    >>> is_Palindrome('qwertyYtrewq') 
    True
    >>> is_Palindrome('1234321')
    True
    >>> is_Palindrome('12345')
    False
    >>> is_Palindrome('abcdefghijklmnopqr')
    False
             
    '''
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
