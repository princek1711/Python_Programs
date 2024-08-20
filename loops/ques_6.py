'''Factorial Calculator
   Problem: Compute the factorial of a number using a while loop.
'''

userInput = int(input("Enter the number you want factorial...."))

count = 1

while userInput > 0:
    count = userInput * count
    userInput-=1

print(count)