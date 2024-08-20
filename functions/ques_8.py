'''<summary>
8. Function with **kwargs
</summary>
Problem: Create a function that accepts any number of keyword arguments and prints
them in the format key: value.
</details'''

def func(**kwargs):
    for key,value in kwargs.items():
        print(key,value)


fun = {"Ram":"Sita","Shiv":"Parvati"}
func(**fun)
# func(Ram="Sita",Shiv = "Parvati")






