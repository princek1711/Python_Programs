''' 1. Basic Function Syntax
</summary>
Problem: Write a function to calculate and return the square of a number.
</details>'''


def power(number,pwr):
    answer = number**pwr
    return answer

askNumber = int(input("Enter the number..."))
askPwr = int(input("Enter power..."))

result = power(askNumber,askPwr)
print(result)
