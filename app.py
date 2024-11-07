''' Sum of numbers from 1 to x using recursion '''
def sumnumbs(x):
    '''This function returns the sum of all numbers from 1 to x'''
    if x == 1: # base case
        return 1
    return sumnumbs(x-1) + x # recursive case

print(sumnumbs(10)) # 55
