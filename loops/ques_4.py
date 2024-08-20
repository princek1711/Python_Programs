# Reverse a String

userInput = input('Enter your string...')


# Reversing the string using a loop
reversed_string = ''
for char in userInput:
    reversed_string = char + reversed_string

print(reversed_string)