''' Find the First Non-Repeated Character
    Problem: Given a string, find the first non-repeated character.
'''
userInput = input('Enter your text here....')

# for char in userInput:
#     if userInput.count(char) == 1:
#         print(char)
#         break


for char in userInput:
    if userInput.count(char)> 1:
        print(char)
        break