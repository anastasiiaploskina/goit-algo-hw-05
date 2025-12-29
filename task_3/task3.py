import timeit
from functools import partial

from boyer_moore import boyer_moore_search
from knuth_morris_pratt import knuth_morris_pratt_search
from rabin_karp import rabin_karp_search


def open_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    return text


def measure_time(func, *args, number=100, **kwargs):
    wrapped = partial(func, *args, **kwargs)
    return float(f"{timeit.timeit(wrapped, number=number):.6f}")


def main():
    filenames = ["text1.txt", "text2.txt"]
    for filename in filenames:
        print(f"\nProccesing file: {filename}")

        text = open_file(filename)

        patterns = [
            "У жадібному алгоритмі завжди робиться вибір, який здається"
            if filename == "text1.txt" else
            "Структура B+ tree показала результати, близькі до хеш-таблиці",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
        ]

        for pattern in patterns:
            print(f"\nSearching for pattern: {pattern}")

            bm_time = measure_time(boyer_moore_search, text, pattern)
            kmp_time = measure_time(knuth_morris_pratt_search, text, pattern)
            rk_time = measure_time(rabin_karp_search, text, pattern)

            print(f"Boyer-Moore time: {bm_time}")
            print(f"Knuth-Morris-Pratt time: {kmp_time}")
            print(f"Rabin-Karp time: {rk_time}")

            times = {
                "Boyer-Moore": bm_time,
                "Knuth-Morris-Pratt": kmp_time,
                "Rabin-Karp": rk_time
            }

            fastest_algorithm = min(times, key=times.get)
            print(f"The fastest algorithm is: {fastest_algorithm} with time {times[fastest_algorithm]}")


if __name__ == "__main__":
    main()
