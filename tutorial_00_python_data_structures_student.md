# Tutorial 0: Python Data Structures - Lists, Sets, Dictionaries, and Tuples

## Introduction

Before diving into algorithmic thinking, it's essential to understand Python's fundamental data structures. This tutorial covers lists, sets, dictionaries, and tuples - when to use each, their differences, and common operations.

## Learning Objectives

By the end of this tutorial, you will be able to:
- Understand the characteristics of each data structure
- Choose the right data structure for different scenarios
- Perform common operations on each structure
- Recognize when to use one over another

## Overview: Quick Comparison

| Data Structure | Ordered | Mutable | Duplicates | Use Case |
|----------------|---------|---------|------------|----------|
| **List** | Yes | Yes | Yes | Ordered collection, need indexing |
| **Tuple** | Yes | No | Yes | Immutable ordered collection |
| **Set** | No | Yes | No | Unique elements, fast membership |
| **Dictionary** | Yes* | Yes | Keys: No, Values: Yes | Key-value pairs, fast lookups |

*Dictionaries maintain insertion order (Python 3.7+)

## 1. Lists

### Characteristics

- **Ordered**: Elements maintain their order
- **Mutable**: Can add, remove, or modify elements
- **Indexed**: Access elements by position (0-based)
- **Allows duplicates**: Same value can appear multiple times
- **Heterogeneous**: Can contain different types

### Creating Lists

```python
# Empty list
empty_list = []
empty_list = list()

# List with elements
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4], [5, 6]]

# List comprehension
squares = [x**2 for x in range(10)]
```

### Common Operations

```python
# Create a list
my_list = [1, 2, 3, 4, 5]

# Access elements
print(my_list[0])      # 1 (first element)
print(my_list[-1])     # 5 (last element)
print(my_list[1:4])    # [2, 3, 4] (slicing)

# Modify elements
my_list[0] = 10        # [10, 2, 3, 4, 5]

# Add elements
my_list.append(6)      # Add to end: [10, 2, 3, 4, 5, 6]
my_list.insert(1, 20)  # Insert at index 1: [10, 20, 2, 3, 4, 5, 6]
my_list.extend([7, 8]) # Extend with another list: [10, 20, 2, 3, 4, 5, 6, 7, 8]

# Remove elements
my_list.remove(20)     # Remove first occurrence of 20
popped = my_list.pop() # Remove and return last element
del my_list[0]         # Remove element at index 0

# Search and count
index = my_list.index(3)  # Find index of first occurrence
count = my_list.count(3)  # Count occurrences
contains = 3 in my_list   # Check membership: True/False

# Sort and reverse
my_list.sort()         # Sort in place
sorted_list = sorted(my_list)  # Return new sorted list
my_list.reverse()      # Reverse in place

# Length
length = len(my_list)  # Get number of elements
```

### When to Use Lists

- Need ordered collection
- Need to access elements by index
- Need to modify the collection
- Order matters
- Duplicates are allowed

**Example**: Shopping cart, to-do list, scores in a game

## 2. Tuples

### Characteristics

- **Ordered**: Elements maintain their order
- **Immutable**: Cannot modify after creation
- **Indexed**: Access elements by position
- **Allows duplicates**: Same value can appear multiple times
- **Faster**: Slightly faster than lists for some operations
- **Hashable**: Can be used as dictionary keys (if all elements are hashable)

### Creating Tuples

```python
# Empty tuple
empty_tuple = ()
empty_tuple = tuple()

# Tuple with elements (note the comma!)
single = (1,)          # Single element tuple (comma required!)
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)

# Without parentheses (tuple packing)
coordinates = 10, 20, 30

# Tuple unpacking
x, y, z = coordinates  # x=10, y=20, z=30
```

### Common Operations

```python
# Create a tuple
my_tuple = (1, 2, 3, 4, 5)

# Access elements (same as lists)
print(my_tuple[0])      # 1
print(my_tuple[-1])     # 5
print(my_tuple[1:4])    # (2, 3, 4)

# Cannot modify (immutable)
# my_tuple[0] = 10      # ERROR! Tuples are immutable

# Search and count
index = my_tuple.index(3)  # Find index
count = my_tuple.count(3)  # Count occurrences
contains = 3 in my_tuple   # Check membership

# Concatenation (creates new tuple)
new_tuple = my_tuple + (6, 7)  # (1, 2, 3, 4, 5, 6, 7)

# Repetition
repeated = my_tuple * 2  # (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Length
length = len(my_tuple)  # Get number of elements
```

### When to Use Tuples

- Need immutable ordered collection
- Want to use as dictionary key
- Returning multiple values from function
- Fixed-size collection
- Slightly better performance than lists

**Example**: Coordinates (x, y, z), RGB color values, database records

## 3. Sets

### Characteristics

- **Unordered**: No guaranteed order (though may appear ordered)
- **Mutable**: Can add or remove elements
- **No duplicates**: Automatically removes duplicates
- **Not indexed**: Cannot access by position
- **Fast membership**: O(1) average case for `in` operation
- **Hashable elements only**: Elements must be immutable

### Creating Sets

```python
# Empty set (note: {} creates a dictionary, not a set!)
empty_set = set()

# Set with elements
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "orange"}

# From list (removes duplicates)
unique_numbers = set([1, 2, 2, 3, 3, 4])  # {1, 2, 3, 4}

# Set comprehension
squares = {x**2 for x in range(10)}
```

### Common Operations

```python
# Create a set
my_set = {1, 2, 3, 4, 5}

# Add elements
my_set.add(6)           # Add single element: {1, 2, 3, 4, 5, 6}
my_set.update([7, 8])   # Add multiple elements: {1, 2, 3, 4, 5, 6, 7, 8}

# Remove elements
my_set.remove(8)        # Remove element (raises error if not found)
my_set.discard(9)       # Remove element (no error if not found)
popped = my_set.pop()   # Remove and return arbitrary element
my_set.clear()          # Remove all elements

# Membership and size
contains = 3 in my_set  # Check membership: True/False
length = len(my_set)    # Get number of elements

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union = set1 | set2              # {1, 2, 3, 4, 5, 6} (all elements)
intersection = set1 & set2       # {3, 4} (common elements)
difference = set1 - set2         # {1, 2} (in set1 but not set2)
symmetric_diff = set1 ^ set2     # {1, 2, 5, 6} (elements in either, not both)

# Subset and superset
is_subset = {1, 2}.issubset(set1)      # True
is_superset = set1.issuperset({1, 2})  # True
```

### When to Use Sets

- Need unique elements
- Fast membership testing
- Set operations (union, intersection, etc.)
- Order doesn't matter
- Removing duplicates

**Example**: Tracking unique visitors, finding common elements, removing duplicates

## 4. Dictionaries

### Characteristics

- **Key-value pairs**: Store data as key:value pairs
- **Ordered**: Maintains insertion order (Python 3.7+)
- **Mutable**: Can add, remove, or modify key-value pairs
- **Keys are unique**: No duplicate keys (later values overwrite earlier)
- **Fast lookups**: O(1) average case for key access
- **Keys must be hashable**: Keys must be immutable (strings, numbers, tuples)

### Creating Dictionaries

```python
# Empty dictionary
empty_dict = {}
empty_dict = dict()

# Dictionary with key-value pairs
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Using dict() constructor
student = dict(name="Alice", age=20, grade="A")

# From list of tuples
pairs = [("name", "Alice"), ("age", 20)]
student = dict(pairs)

# Dictionary comprehension
squares = {x: x**2 for x in range(10)}
```

### Common Operations

```python
# Create a dictionary
my_dict = {"name": "Alice", "age": 20, "city": "New York"}

# Access values
name = my_dict["name"]           # "Alice"
age = my_dict.get("age")         # 20
age = my_dict.get("age", 0)      # 20 (with default if key missing)
age = my_dict.get("salary", 0)   # 0 (key doesn't exist, returns default)

# Modify values
my_dict["age"] = 21              # Update existing key
my_dict["salary"] = 50000        # Add new key-value pair

# Add/Update multiple items
my_dict.update({"age": 22, "city": "Boston"})

# Remove items
del my_dict["city"]               # Remove key-value pair
removed = my_dict.pop("age")      # Remove and return value
removed = my_dict.pop("age", 0)   # With default if key missing
my_dict.clear()                   # Remove all items

# Check membership
has_key = "name" in my_dict       # True
has_key = "salary" in my_dict     # False

# Get keys, values, items
keys = my_dict.keys()             # dict_keys(['name', 'age'])
values = my_dict.values()         # dict_values(['Alice', 20])
items = my_dict.items()           # dict_items([('name', 'Alice'), ('age', 20)])

# Iterate
for key in my_dict:
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(key, value)

# Length
length = len(my_dict)             # Number of key-value pairs
```

### When to Use Dictionaries

- Need key-value mapping
- Fast lookups by key
- Storing structured data
- Counting frequencies
- Caching/memoization

**Example**: Student records, word frequency counter, configuration settings

## Detailed Comparison

### Memory and Performance

```python
import sys

# Memory usage
list_example = [1, 2, 3, 4, 5]
tuple_example = (1, 2, 3, 4, 5)
set_example = {1, 2, 3, 4, 5}
dict_example = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}

print(f"List size: {sys.getsizeof(list_example)} bytes")
print(f"Tuple size: {sys.getsizeof(tuple_example)} bytes")
print(f"Set size: {sys.getsizeof(set_example)} bytes")
print(f"Dict size: {sys.getsizeof(dict_example)} bytes")
```

### Time Complexity Comparison

| Operation | List | Tuple | Set | Dictionary |
|-----------|------|-------|-----|------------|
| Access by index/key | O(1) | O(1) | N/A | O(1) |
| Search (in) | O(n) | O(n) | O(1) | O(1) |
| Insert | O(1)* | N/A | O(1) | O(1) |
| Delete | O(n)* | N/A | O(1) | O(1) |
| Sort | O(n log n) | N/A | N/A | N/A |

*Amortized O(1) for append, O(n) for insert/delete at arbitrary position

## Measuring Execution Time

Understanding how long operations take is crucial for writing efficient code. Python provides several ways to measure execution time.

### Using `time.time()`

```python
import time

# Measure time for list membership check
my_list = list(range(1000000))
target = 999999

start_time = time.time()
result = target in my_list
end_time = time.time()

elapsed = end_time - start_time
print(f"List membership check took {elapsed:.6f} seconds")
print(f"Result: {result}")
```

### Using `timeit` Module (Recommended)

The `timeit` module provides more accurate timing by running code multiple times and averaging:

```python
import timeit

# Compare list vs set membership
my_list = list(range(100000))
my_set = set(range(100000))
target = 99999

# Time list membership (O(n))
list_time = timeit.timeit(lambda: target in my_list, number=1000)
print(f"List membership (1000 runs): {list_time:.6f} seconds")
print(f"Average per run: {list_time/1000:.9f} seconds")

# Time set membership (O(1))
set_time = timeit.timeit(lambda: target in my_set, number=1000)
print(f"Set membership (1000 runs): {set_time:.6f} seconds")
print(f"Average per run: {set_time/1000:.9f} seconds")

print(f"\nSet is {list_time/set_time:.1f}x faster!")
```

### Practical Example: Comparing Data Structure Operations

```python
import timeit

# Setup
n = 100000
test_list = list(range(n))
test_set = set(range(n))
test_dict = {i: i*2 for i in range(n)}

# Test 1: Membership checking
print("=== Membership Testing ===")
list_membership = timeit.timeit(lambda: n-1 in test_list, number=1000)
set_membership = timeit.timeit(lambda: n-1 in test_set, number=1000)
dict_membership = timeit.timeit(lambda: n-1 in test_dict, number=1000)

print(f"List:  {list_membership:.6f} seconds (O(n))")
print(f"Set:   {set_membership:.6f} seconds (O(1))")
print(f"Dict:  {dict_membership:.6f} seconds (O(1))")
print(f"Set is {list_membership/set_membership:.1f}x faster than list")

# Test 2: Adding elements
print("\n=== Adding Elements ===")
list_append = timeit.timeit(lambda: test_list.append(999999), number=10000)
set_add = timeit.timeit(lambda: test_set.add(999999), number=10000)
dict_set = timeit.timeit(lambda: test_dict.update({999999: 1999998}), number=10000)

print(f"List append: {list_append:.6f} seconds")
print(f"Set add:     {set_add:.6f} seconds")
print(f"Dict update: {dict_set:.6f} seconds")

# Test 3: Iteration
print("\n=== Iteration ===")
list_iter = timeit.timeit(lambda: [x for x in test_list[:1000]], number=1000)
set_iter = timeit.timeit(lambda: [x for x in list(test_set)[:1000]], number=1000)
dict_iter = timeit.timeit(lambda: [v for k, v in list(test_dict.items())[:1000]], number=1000)

print(f"List iteration:  {list_iter:.6f} seconds")
print(f"Set iteration:   {set_iter:.6f} seconds")
print(f"Dict iteration:  {dict_iter:.6f} seconds")
```

**Run this code and observe the timing differences!** You'll see that sets and dictionaries are much faster for membership testing, while lists are faster for iteration.

## NumPy vs Pure Python: Performance Comparison

NumPy (Numerical Python) is a powerful library for numerical computations. It's significantly faster than pure Python for array operations. Let's see why!

### Why NumPy is Faster

1. **Vectorization**: Operations are applied to entire arrays at once, not element-by-element
2. **C Implementation**: Core operations are written in C/C++, which is much faster than Python
3. **Memory Efficiency**: Arrays are stored contiguously in memory, improving cache performance
4. **No Type Checking**: NumPy arrays have fixed types, eliminating Python's dynamic type checking overhead

### Comparison: Array Operations

```python
import numpy as np
import timeit

# Create large arrays/lists
size = 1000000
python_list = list(range(size))
numpy_array = np.arange(size)

# Test 1: Element-wise addition
print("=== Element-wise Addition ===")

def python_add():
    return [x + 10 for x in python_list]

def numpy_add():
    return numpy_array + 10

python_time = timeit.timeit(python_add, number=10)
numpy_time = timeit.timeit(numpy_add, number=10)

print(f"Python list: {python_time:.6f} seconds")
print(f"NumPy array: {numpy_time:.6f} seconds")
print(f"NumPy is {python_time/numpy_time:.1f}x faster!")

# Test 2: Sum of elements
print("\n=== Sum of Elements ===")

def python_sum():
    return sum(python_list)

def numpy_sum():
    return np.sum(numpy_array)

python_time = timeit.timeit(python_sum, number=100)
numpy_time = timeit.timeit(numpy_sum, number=100)

print(f"Python sum(): {python_time:.6f} seconds")
print(f"NumPy sum():  {numpy_time:.6f} seconds")
print(f"NumPy is {python_time/numpy_time:.1f}x faster!")

# Test 3: Finding maximum
print("\n=== Finding Maximum ===")

def python_max():
    return max(python_list)

def numpy_max():
    return np.max(numpy_array)

python_time = timeit.timeit(python_max, number=100)
numpy_time = timeit.timeit(numpy_max, number=100)

print(f"Python max(): {python_time:.6f} seconds")
print(f"NumPy max():  {numpy_time:.6f} seconds")
print(f"NumPy is {python_time/numpy_time:.1f}x faster!")
```

### Comparison: Mathematical Operations

```python
import numpy as np
import timeit
import math

size = 1000000
python_list = [i * 0.1 for i in range(size)]
numpy_array = np.arange(size) * 0.1

# Test: Square root of all elements
print("=== Square Root Operation ===")

def python_sqrt():
    return [math.sqrt(x) for x in python_list]

def numpy_sqrt():
    return np.sqrt(numpy_array)

python_time = timeit.timeit(python_sqrt, number=10)
numpy_time = timeit.timeit(numpy_sqrt, number=10)

print(f"Python: {python_time:.6f} seconds")
print(f"NumPy:  {numpy_time:.6f} seconds")
print(f"NumPy is {python_time/numpy_time:.1f}x faster!")

# Test: Element-wise multiplication
print("\n=== Element-wise Multiplication ===")

def python_multiply():
    return [x * 2.5 for x in python_list]

def numpy_multiply():
    return numpy_array * 2.5

python_time = timeit.timeit(python_multiply, number=10)
numpy_time = timeit.timeit(numpy_multiply, number=10)

print(f"Python: {python_time:.6f} seconds")
print(f"NumPy:  {numpy_time:.6f} seconds")
print(f"NumPy is {python_time/numpy_time:.1f}x faster!")
```

### Why Pure Python Takes More Time

1. **Interpreted vs Compiled**: Python is interpreted line-by-line, while NumPy operations are pre-compiled C code
2. **Type Checking Overhead**: Python checks types at runtime for every operation
3. **Memory Overhead**: Python lists store pointers to objects, while NumPy arrays store raw data
4. **Loop Overhead**: Python loops have overhead for each iteration (checking conditions, incrementing counters)
5. **No Vectorization**: Pure Python processes elements one at a time, while NumPy uses SIMD (Single Instruction Multiple Data) instructions

### Visual Comparison Example

```python
import numpy as np
import timeit

# Create arrays
size = 1000000
python_list = list(range(size))
numpy_array = np.arange(size, dtype=np.int32)

print("=== Comprehensive Performance Test ===\n")

operations = [
    ("Addition", lambda: [x + 1 for x in python_list], lambda: numpy_array + 1),
    ("Multiplication", lambda: [x * 2 for x in python_list], lambda: numpy_array * 2),
    ("Sum", lambda: sum(python_list), lambda: np.sum(numpy_array)),
    ("Mean", lambda: sum(python_list) / len(python_list), lambda: np.mean(numpy_array)),
]

for op_name, python_func, numpy_func in operations:
    python_time = timeit.timeit(python_func, number=10)
    numpy_time = timeit.timeit(numpy_func, number=10)
    speedup = python_time / numpy_time if numpy_time > 0 else 0
    
    print(f"{op_name:15} | Python: {python_time:8.6f}s | NumPy: {numpy_time:8.6f}s | Speedup: {speedup:6.1f}x")
```

**Run this code to see dramatic performance differences!** NumPy is typically 10-100x faster for numerical operations.

### When to Use NumPy vs Pure Python

**Use NumPy when:**
- Working with large numerical arrays
- Performing mathematical operations on arrays
- Need maximum performance for numerical computations
- Working with multi-dimensional data

**Use Pure Python when:**
- Working with small datasets
- Need heterogeneous data types
- Operations don't involve numerical computations
- Code readability and simplicity are priorities

### Memory Comparison

```python
import sys
import numpy as np

size = 1000000

python_list = list(range(size))
numpy_array = np.arange(size, dtype=np.int32)

print("=== Memory Usage ===")
print(f"Python list: {sys.getsizeof(python_list) / (1024*1024):.2f} MB")
print(f"NumPy array: {numpy_array.nbytes / (1024*1024):.2f} MB")
print(f"NumPy uses {sys.getsizeof(python_list) / numpy_array.nbytes:.1f}x less memory!")

# Python list stores pointers (8 bytes each on 64-bit systems)
# NumPy array stores actual integers (4 bytes each for int32)
```

### Practical Exercise: Measure Your Own Operations

Try measuring the time for these operations yourself:

```python
import timeit
import numpy as np

# Exercise: Compare these operations
size = 100000

# 1. Create list vs numpy array
python_list = list(range(size))
numpy_array = np.arange(size)

# TODO: Measure creation time
# TODO: Measure memory usage
# TODO: Measure access time (accessing middle element)
# TODO: Measure slicing time
# TODO: Measure sorting time

# Write your timing code here!
```

## Practical Examples

### Example 1: Choosing the Right Structure

**Scenario**: Track unique student IDs who attended a class

```python
# Use SET - we need unique values and fast membership checking
attended = {101, 102, 103, 101, 104}  # Duplicate 101 automatically removed
print(attended)  # {101, 102, 103, 104}

# Check if student attended
if 101 in attended:
    print("Student 101 attended")
```

**Scenario**: Store student information (ID -> name mapping)

```python
# Use DICTIONARY - key-value pairs for lookups
students = {
    101: "Alice",
    102: "Bob",
    103: "Charlie"
}

# Fast lookup by ID
name = students[101]  # "Alice"
```

**Scenario**: Maintain ordered list of tasks

```python
# Use LIST - order matters, may have duplicates
tasks = ["homework", "study", "homework", "exercise"]
tasks.append("sleep")  # Add to end
first_task = tasks[0]  # Access by position
```

**Scenario**: Store fixed coordinates

```python
# Use TUPLE - immutable, fixed size
point = (10, 20, 30)  # x, y, z coordinates
x, y, z = point       # Unpack
```

### Example 2: Counting Frequencies

```python
# Problem: Count frequency of each word in a sentence

sentence = "the quick brown fox jumps over the lazy dog"

# Approach 1: Using dictionary
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)
# Output: {'the': 2, 'quick': 1, 'brown': 1, ...}

# Approach 2: Using Counter (from collections)
from collections import Counter
word_count = Counter(sentence.split())
print(word_count)
```

### Example 3: Finding Common Elements

```python
# Problem: Find students who took both Math and Science

math_students = {"Alice", "Bob", "Charlie", "David"}
science_students = {"Bob", "David", "Eve", "Frank"}

# Use set intersection
both_classes = math_students & science_students
print(both_classes)  # {'Bob', 'David'}
```

### Example 4: Removing Duplicates

```python
# Problem: Get unique values from a list

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Method 1: Convert to set (loses order)
unique = list(set(numbers))  # Order may change

# Method 2: Preserve order (Python 3.7+)
unique = list(dict.fromkeys(numbers))  # [1, 2, 3, 4]

# Method 3: Using list comprehension (preserve order)
seen = set()
unique = [x for x in numbers if not (x in seen or seen.add(x))]
```

## Common Mistakes and Pitfalls

### Mistake 1: Confusing {} for Sets

```python
# WRONG: This creates a dictionary, not a set!
empty = {}  # This is a dict!
print(type(empty))  # <class 'dict'>

# CORRECT: Use set() for empty set
empty = set()
print(type(empty))  # <class 'set'>
```

### Mistake 2: Modifying Tuple

```python
# WRONG: Tuples are immutable
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # ERROR!

# CORRECT: Create new tuple
my_tuple = (10, 2, 3)
```

### Mistake 3: Using List as Dictionary Key

```python
# WRONG: Lists are not hashable
# my_dict = {[1, 2]: "value"}  # ERROR!

# CORRECT: Use tuple instead
my_dict = {(1, 2): "value"}  # OK!
```

### Mistake 4: Assuming Set Order

```python
# Sets are unordered - don't rely on order!
my_set = {3, 1, 4, 1, 5, 9, 2, 6}
# Order may vary: {1, 2, 3, 4, 5, 6, 9}
```

## Practice Exercises

### Exercise 1: Data Structure Selection

For each scenario, choose the best data structure and explain why:

1. **Tracking unique email addresses of newsletter subscribers**
   - Your choice: __________
   - Why: __________

2. **Storing a sequence of moves in a chess game**
   - Your choice: __________
   - Why: __________

3. **Mapping student IDs to their exam scores**
   - Your choice: __________
   - Why: __________

4. **Storing RGB color values (red, green, blue)**
   - Your choice: __________
   - Why: __________

### Exercise 2: Implement Functions

**Problem 1**: Write a function that takes a list and returns a new list with duplicates removed while preserving order.

```python
def remove_duplicates_preserve_order(lst):
    """
    Remove duplicates from list while preserving order.
    
    Args:
        lst: List with possible duplicates
    
    Returns:
        List with duplicates removed, order preserved
    """
    # TODO: Implement this function
    pass

# Test cases
# remove_duplicates_preserve_order([1, 2, 2, 3, 3, 3, 4]) should return [1, 2, 3, 4]
# remove_duplicates_preserve_order(['a', 'b', 'a', 'c', 'b']) should return ['a', 'b', 'c']
```

**Problem 2**: Write a function that finds the intersection of two lists (common elements).

```python
def find_intersection(list1, list2):
    """
    Find common elements between two lists.
    
    Args:
        list1: First list
        list2: Second list
    
    Returns:
        List of common elements (no duplicates)
    """
    # TODO: Implement this function
    pass

# Test cases
# find_intersection([1, 2, 3, 4], [3, 4, 5, 6]) should return [3, 4] or [4, 3]
# find_intersection(['a', 'b', 'c'], ['b', 'c', 'd']) should return ['b', 'c'] or ['c', 'b']
```

**Problem 3**: Write a function that counts the frequency of each character in a string.

```python
def count_characters(text):
    """
    Count frequency of each character in string.
    
    Args:
        text: Input string
    
    Returns:
        Dictionary mapping character to its count
    """
    # TODO: Implement this function
    pass

# Test cases
# count_characters("hello") should return {'h': 1, 'e': 1, 'l': 2, 'o': 1}
# count_characters("aabbcc") should return {'a': 2, 'b': 2, 'c': 2}
```

**Problem 4**: Write a function that groups words by their first letter.

```python
def group_by_first_letter(words):
    """
    Group words by their first letter.
    
    Args:
        words: List of words
    
    Returns:
        Dictionary mapping first letter to list of words starting with that letter
    """
    # TODO: Implement this function
    pass

# Test cases
# group_by_first_letter(["apple", "banana", "apricot", "blueberry"])
# Should return {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}
```

**Problem 5**: Write a function that checks if two lists contain the same elements (ignoring order and duplicates).

```python
def have_same_elements(list1, list2):
    """
    Check if two lists contain the same elements (ignoring order and duplicates).
    
    Args:
        list1: First list
        list2: Second list
    
    Returns:
        True if lists contain same elements, False otherwise
    """
    # TODO: Implement this function
    pass

# Test cases
# have_same_elements([1, 2, 3], [3, 2, 1]) should return True
# have_same_elements([1, 2, 2, 3], [1, 2, 3]) should return True
# have_same_elements([1, 2, 3], [1, 2, 4]) should return False
```

### Exercise 3: Analyze and Optimize

**Problem**: You have a function that checks if a number exists in a list. The list has 1 million elements and you need to check membership frequently.

```python
def number_exists_naive(numbers, target):
    """
    Check if target exists in numbers.
    Current implementation uses list.
    """
    return target in numbers  # O(n) - slow for large lists!

# How can you optimize this? What data structure would you use?
# TODO: Write an optimized version
```

### Exercise 4: Real-World Application

**Problem**: Design a data structure to manage a library system. You need to:
- Track which books are available (by ISBN)
- Store book information (title, author) by ISBN
- Maintain a waiting list for popular books (ordered by request time)
- Track which members have borrowed which books

```python
# TODO: Design the data structures
# Hint: You'll likely need multiple data structures working together

# Available books (ISBNs)
available_books = None  # TODO: Choose appropriate structure

# Book information (ISBN -> details)
book_info = None  # TODO: Choose appropriate structure

# Waiting list for each book (ISBN -> ordered list of member IDs)
waiting_lists = None  # TODO: Choose appropriate structure

# Member borrowings (member ID -> set of ISBNs)
member_borrowings = None  # TODO: Choose appropriate structure
```

## Practice Time!

**Great work!** You've reached the practice exercises.

Try to solve the problems above on your own before checking solutions.
When you're ready, you can:
- Check the solutions in the original markdown file
- Ask your instructor for help
- Discuss with classmates

Remember: The process of solving is more important than getting the answer immediately!

## Practice Time!

**Great work!** You've learned about Python's fundamental data structures. Try to solve the exercises above on your own before checking solutions.

When you're ready, you can:
- Check the solutions above
- Ask your instructor for help
- Discuss with classmates

Remember: Understanding when to use each data structure is crucial for writing efficient algorithms!

## Key Takeaways

1. **Lists**: Ordered, mutable, indexed - use when order matters and you need to modify
2. **Tuples**: Ordered, immutable - use for fixed data, dictionary keys, or when immutability is needed
3. **Sets**: Unordered, unique elements - use for fast membership testing and set operations
4. **Dictionaries**: Key-value pairs - use for fast lookups and structured data
5. **Choose wisely**: The right data structure can make your code faster and clearer
6. **Understand trade-offs**: Each structure has different time/space complexities

## Quick Reference Cheat Sheet

```python
# LIST
my_list = [1, 2, 3]
my_list.append(4)
my_list[0] = 10

# TUPLE
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # ERROR - immutable!

# SET
my_set = {1, 2, 3}
my_set.add(4)
3 in my_set  # Fast membership check

# DICTIONARY
my_dict = {"a": 1, "b": 2}
my_dict["c"] = 3
value = my_dict.get("a", 0)
```

## Next Steps

Now that you understand Python's data structures, you're ready for **Tutorial 1: Introduction to Algorithmic Thinking**, where you'll learn how to use these structures to solve problems algorithmically!
