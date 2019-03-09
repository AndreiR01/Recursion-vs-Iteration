#Iterative Solution
def factorial(n):
    if n<0:
        ValueError("Inputs of 0 or grater!")
    result = 1
    while n != 0:
        result *= n
        n -= 1
    return result

#Recursive Solution

def factorial(n):
    if n<0:
        ValueError("Inputs of 0 or grater!")
    elif n <= 1:
        return 1
    return n * factorial(n-1)
    
