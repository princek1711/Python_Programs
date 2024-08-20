'''Problem 1: Timing Function Execution
</summary>
Problem: Write a decorator that measures the time a function takes to execute.
</details>
'''

import time


def timer(func):
    def warrper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return warrper


@timer
def result(n):
    time.sleep(n)

result(3)

