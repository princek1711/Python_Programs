''' Validate Input
    Problem: Keep asking the user for input until they enter a number between 1 and 10.
'''

userInput = int(input("Enter the number between 1 to 10..."))

while True: 
 if userInput <=10:
     print(userInput)
     break
 else:
      userInput = int(input("Enter the number between 1 to 10 only..."))

