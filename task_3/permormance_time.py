import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        elapsed = end - start
        print(f"\nExecution time: {elapsed:.3f} seconds")
        return result
    return wrapper


import time


def measure_time_ns(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end = time.perf_counter_ns()

        elapsed = end - start
        print(f"\nExecution time: {elapsed:} nanoseconds")
        return result
    return wrapper


import time


def measure_time_ms(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end = time.perf_counter_ns()

        elapsed = (end - start) / 1000
        print(f"\nExecution time: {elapsed:} microseconds")
        return result
    return wrapper
