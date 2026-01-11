
# **Algorithms 5**

This repository contains a hash table, a binary search function, and a comparison analysis of Boyer-Moore, Knuth-Morris-Pratt, and Rabin-Karp algorithms.

---

## **Table of Contents**

* [Task 1 - Hash Table](#task-1-hash-table)
* [Task 2 - Binary Search](#task-2-sort-nested-lists)
* [Task 3 - Pattern Searching Algorithms](#benchmark-data-factories)
* [Results](#results)

---

# **Task 1 - Hash Table**

### **Example Usage**

```python
if __name__ == "__main__":
    try:
        H = HashTable(5)
        H.insert("apple", 10)
        H.insert("orange", 20)
        H.insert("banana", 30)

        assert H.get("apple") == 10
        assert H.get("orange") == 20
        assert H.get("banana") == 30

        assert H.delete("orange") is True
        assert H.get("orange") is None
        assert H.delete("grape") is False

    except AssertionError:
        print("Assertation failed!")
    else:
        print("All tests passed successfully!")
```
---

# **Task 2 - Binary Search**

### **Key Functions**

#### **1. measure_time()**

Counts time performance, works as a decorator


#### **2. binary_search(numbers)**

Searches for a number within a list, receives a list as an argument, returns the number of steps and the closest found number.

### **Example Usage**

```python
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
```

---

# **Task 3 - Pattern Searching Algorithms**

The task was to identify existing and non-existent patterns within two texts.

### **Key Functions**

#### **1. boyer_moore_search()**

#### **2. knuth_morris_pratt_search()**

#### **3. rabin_karp_search()**

### **Example Usage**
```
Processing file: text1.txt

Searching for pattern: У жадібному алгоритмі завжди робиться вибір, який здається
Boyer-Moore time: 0.004746
Knuth-Morris-Pratt time: 0.041958
Rabin-Karp time: 0.089806
The fastest algorithm is: Boyer-Moore with time 0.004746

Searching for pattern: Lorem ipsum dolor sit amet, consectetur adipiscing elit
Boyer-Moore time: 0.003946
Knuth-Morris-Pratt time: 0.04816
Rabin-Karp time: 0.127604
The fastest algorithm is: Boyer-Moore with time 0.003946

Processing file: text2.txt

Searching for pattern: Структура B+ tree показала результати, близькі до хеш-таблиці
Boyer-Moore time: 0.008318
Knuth-Morris-Pratt time: 0.069049
Rabin-Karp time: 0.141613
The fastest algorithm is: Boyer-Moore with time 0.008318

Searching for pattern: Lorem ipsum dolor sit amet, consectetur adipiscing elit
Boyer-Moore time: 0.00468
Knuth-Morris-Pratt time: 0.068133
Rabin-Karp time: 0.181329
The fastest algorithm is: Boyer-Moore with time 0.00468
```

---

# **Results**
* We can see that, no matter what, the Boyer-Moore algorithm is the most efficient when searching for both existing and non-existent patterns within texts

---

# **Dependencies**

This project uses only the Python standard library:

* `time`
* `timeit`
* `partial`

No external installations required.
