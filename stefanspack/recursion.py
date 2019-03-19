def sum_array(array):

    '''Return sum of all items in array'''

    # If statement to ensure function does not loop infinitely.
    if len(array)==0:
        return 0

    # Else statement to activate recursion to sum array
    else:
        return array[0] + sum_array(array[1:])


def fibonacci(n):

    '''Return nth term in fibonacci sequence'''

    # If statement to ensure function does not loop infinitely.
    if n <= 1:
        return n

    # Else statement to activate recursion to determine nth term in fibonacci sequence.
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    '''Return n!'''

    # If statement to ensure function does not loop infinitely.
    if n <= 1:
        return n

    # Else statement to activate recursion to calculate factorial
    else:
        return n * factorial(n-1)


def reverse(word):

    '''Return word in reverse'''

    # If statement to ensure function does not loop infinitely.
    if word == '':
        return word

    # Else statement to activate recursion on word
    else:
        return word[-1] + reverse(word[:-1])
