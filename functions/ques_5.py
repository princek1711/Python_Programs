'''5. Default Parameter Value
</summary>
Problem: Write a function that greets a user. 
If no name is provided, it should greet with 
a default name.
</details>
'''

askFromUser = input("Enter your name.....")

def greet(name): 
    if name == "":
        print('Hello user!')
    else:
         print("Hello " , name, "!")

greet(askFromUser)

