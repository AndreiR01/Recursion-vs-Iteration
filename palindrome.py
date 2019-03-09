 #palindromes - words whoch read the same the same foward and backwards

#Iterative solution
#O(N^2) - in each iteration of the loop that doesnt rreturn False, we make a copy of the strings with two fewer characters
def is_palindrome(my_string):

    while len(my_string) > 1:
        if my_string[0] != my_string[-1]:
          return False
        my_string = my_string[1:-1]
    return True

palindrome("abba")
# True
palindrome("abcba")
# True
palindrome("")
# True
palindrome("abcd")
# False
#------------------------------

#More efficient iterative solution
#O(N)
# Linear - O(N)
def is_palindrome(my_string):
    string_length = len(my_string)
    middle_index = string_length // 2
        for index in range(0, middle_index):
          opposite_character_index = string_length - index
          if my_string[index] != my_string[opposite_character_index]
        return False
return True
#--------------------------

#Recursive solution
def is_palindrome(str):
    if len(str) < 2:
        return True
    if str[0] != str[-1]:
        return False
    return is_palindrome(str[1:-1])


# test cases
print(is_palindrome("abba") == True)
print(is_palindrome("abcba") == True)
print(is_palindrome("") == True)
print(is_palindrome("abcd") == False)
