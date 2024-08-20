'''<details>
<summary>
Problem 2: Debugging Function Calls
</summary>
Problem: Create a decorator to print the function name and the values of its 
arguments every time the function is called.
</details>'''

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def hello():
    print("Namaste")

@debug
def greeting(name, greet = "Namaste Again !"):
    print(f"{name},{greet}")

hello()
greeting("Prince","Namaste  Again!")