import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end = time.perf_counter_ns()

        elapsed = end - start
        print(f"\nExecution time: {elapsed} nanoseconds")
        return result
    return wrapper


@measure_time
def binary_search(arr: list, target: float) -> tuple:
    iter = 0
    low, high = 0, len(arr) - 1
    upper_bound = None

    while low <= high:
        iter += 1
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            upper_bound = arr[mid]
            high = mid - 1
        else:
            upper_bound = arr[mid]
            break

    return (iter, upper_bound) if upper_bound is not None else (iter, -1)


numbers = [0.12, 0.35, 0.58, 1.03, 1.27,
           1.49, 1.88, 2.01, 2.34, 2.79,
           3.14, 3.56, 4.02, 4.44, 4.99]


if __name__ == "__main__":
    try:
        assert binary_search(numbers, 2.01) == (1, 2.01)
        assert binary_search(numbers, 1.03) == (2, 1.03)
        assert binary_search(numbers, 5.50) == (4, -1)
        assert binary_search(numbers, 2.50) == (4, 2.79)
        assert binary_search(numbers, 0.50) == (4, 0.58)
        assert binary_search(numbers, 3.14) == (4, 3.14)

    except AssertionError:
        print("Assertation failed!")
    else:
        print("All tests passed successfully!")
