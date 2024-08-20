'''
    List Uniqueness Checker
    Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
'''

items = ["apple", "banana", "orange", "mango"]

for item in items:
    if items.count(item) >1:
        print('Duplicate')
        break
    # print(items.count(item))