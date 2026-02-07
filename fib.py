#fib.py
from functools import lru_cache
import time
import matplotlib.pyplot as plt

tracked_times = []
iteration = []

def timer():
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()

            time_elapsed = end_time - start_time
            tracked_times.append(time_elapsed)
            print(f"Finished in {time_elapsed:.8f} seconds f({args[0]}) -> {result}")
            return result
        return wrapper
    return decorator

@lru_cache(maxsize=None)
@timer()
def fib(n: int) -> int:
    iteration.insert(0, n)
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
    

if __name__ == "__main__":
    fib(100)

    plt.plot(iteration, tracked_times)
    plt.show()