#!/usr/bin/python3
""" Module required for this task"""
def minOperations(n):
    """
    minOperations
    Gets less numbers of operations needed to result in exactly n H characters
    """
    # all displays should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    operations, header = 0, 2
    while header <= n:
        #modulus to deal with remainders
        if n % header == 0:
            
            operations += header
            # set n to the remainder 
            n = n / header
            
            header -= 1
       
        header += 1
    return operations

