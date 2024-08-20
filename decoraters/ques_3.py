'''<details>
<summary>
Problem 3: Cache Return Values
</summary>
Problem: Implement a decorator that caches the return values of a function, so 
that when it's called with the same arguments, the cached value is returned instead 
of re-executing the function.
</details>'''
import time

def cache(func):
    cacheValue = {}
    print(cacheValue)
    def wrapper(*args,**kwargs):
        if args in cacheValue:
            return cacheValue[args]
        result = func(*args)
        cacheValue[args] = result
        return result
    return wrapper  
    
@cache
def function(a,b):
    time.sleep(4)
    return a + b


print(function(2,3))
print(function(2,3))
print(function(4,5))
print(function('Ram','Sita'))