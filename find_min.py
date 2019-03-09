#Recursive solution
def sum_digits(n):
  if n < 0:
    ValueError("Inputs 0 or greater only!")
  #base case
  if n <= 9:
    return n
  #recursive function
  last_digit = n % 10
  return sum_digits(n//10) + last_digit



#Iterative Solution

# Linear - O(N)
def sum_digits(n):
  if n < 0:
    ValueError("Inputs 0 or greater only!")
  result = 0
  while n is not 0:
    result += n % 10
    n = n // 10
  return result + n

sum_digits(12)
# 1 + 2
# 3
sum_digits(552)
# 5 + 5 + 2
# 12
sum_digits(123456789)
# 1 + 2 + 3 + 4...
# 45
