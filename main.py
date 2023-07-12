def is_palindrome(input_string):
    reversed_string = input_string[::-1]
    return input_string == reversed_string

print(is_palindrome("лепсспел"))  # Вернет True
print(is_palindrome("helloworld"))  # Вернет False
