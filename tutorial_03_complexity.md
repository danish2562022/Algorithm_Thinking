# Tutorial 3: Time and Space Complexity

## Introduction

Understanding complexity is crucial for writing efficient algorithms. This tutorial teaches you how to analyze the time and space requirements of your code using Big O notation.

## What is Complexity?

**Time Complexity**: How the runtime of an algorithm grows as the input size increases.

**Space Complexity**: How much memory an algorithm uses as the input size increases.

## Big O Notation

Big O notation describes the **worst-case** performance of an algorithm. It focuses on how performance scales with input size, ignoring constants and lower-order terms.

### Why Big O?

- **Scalability**: Helps predict how algorithms perform on large inputs
- **Comparison**: Allows comparing different approaches objectively
- **Optimization**: Identifies bottlenecks in your code

## Common Complexity Classes

### O(1) - Constant Time

The algorithm takes the same amount of time regardless of input size.

```python
def get_first_element(arr):
    """Always takes the same time - just accessing an index"""
    return arr[0] if arr else None

def add_to_dict(dictionary, key, value):
    """Dictionary insertion is O(1) on average"""
    dictionary[key] = value
```

**Example**: Accessing an array/list element, hash/dictionary lookup, adding to a set.

### O(log n) - Logarithmic Time

The runtime grows logarithmically with input size. Very efficient!

```python
def binary_search(arr, target):
    """
    Binary search: O(log n)
    Each step eliminates half of the remaining elements
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Example: Searching in array/list of 1,000,000 elements
# Takes about 20 comparisons (log2(1,000,000) ≈ 20)
```

**Example**: Binary search, balanced tree operations.

### O(n) - Linear Time

Runtime grows proportionally with input size.

```python
def find_max(arr):
    """Must check every element once"""
    max_val = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num
    return max_val

def sum_array(arr):
    """Must add every element"""
    total = 0
    for num in arr:
        total += num
    return total
```

**Example**: Iterating through an array/list, finding an element in an unsorted array/list.

### O(n log n) - Linearithmic Time

Common in efficient sorting algorithms.

```python
def merge_sort(arr):
    """
    Merge sort: O(n log n)
    Divide: O(log n) levels
    Merge: O(n) work at each level
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**Example**: Merge sort, heap sort, efficient sorting algorithms.

### O(n²) - Quadratic Time

Runtime grows with the square of input size. Often involves nested loops.

```python
def bubble_sort(arr):
    """
    Bubble sort: O(n²)
    Outer loop: n iterations
    Inner loop: up to n iterations
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def find_duplicates(arr):
    """Check every pair"""
    duplicates = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                duplicates.append(arr[i])
    return duplicates
```

**Example**: Nested loops, bubble sort, selection sort.

### O(2ⁿ) - Exponential Time

Runtime doubles with each additional input element. Very inefficient!

```python
def fibonacci_naive(n):
    """
    Naive recursive Fibonacci: O(2ⁿ)
    Each call makes two more calls
    """
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)

# This is VERY slow for large n!
# fibonacci_naive(40) takes a very long time
```

**Example**: Naive recursive solutions, brute force algorithms.

## Visualizing Complexity

```
Input Size (n)    O(1)    O(log n)    O(n)    O(n log n)    O(n²)    O(2ⁿ)
─────────────────────────────────────────────────────────────────────────────
10                1       3           10      33           100      1024
100               1       7           100     664          10,000   1.27×10³⁰
1,000             1       10          1,000   9,966        1M       (huge!)
10,000            1       13          10K     132K         100M     (impossible!)
```

## Analyzing Code Complexity

### Rules of Thumb

1. **Sequential operations**: Add complexities
   ```python
   # O(n) + O(n) = O(n) - still linear
   def example(arr):
       max_val = max(arr)      # O(n)
       min_val = min(arr)      # O(n)
       return max_val, min_val
   ```

2. **Nested operations**: Multiply complexities
   ```python
   # O(n) × O(n) = O(n²)
   def example(arr):
       for i in arr:           # O(n)
           for j in arr:       # O(n)
               print(i, j)
   ```

3. **Drop constants**: O(2n) = O(n), O(n/2) = O(n)
   ```python
   # O(2n) simplifies to O(n)
   def example(arr):
       for x in arr:           # O(n)
           print(x)
       for x in arr:           # O(n)
           print(x)
   ```

4. **Drop lower-order terms**: O(n² + n) = O(n²)
   ```python
   # O(n² + n) simplifies to O(n²)
   def example(arr):
       for i in arr:           # O(n²)
           for j in arr:
               print(i, j)
       for x in arr:           # O(n)
           print(x)
   ```

## Space Complexity

Space complexity measures how much memory an algorithm uses.

### O(1) - Constant Space

```python
def find_max(arr):
    """Only uses a few variables, regardless of input size"""
    max_val = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num
    return max_val
```

### O(n) - Linear Space

```python
def copy_array(arr):
    """Creates a new array/list of same size"""
    return arr.copy()

def reverse_array(arr):
    """Creates a new array/list"""
    result = []
    for i in range(len(arr) - 1, -1, -1):
        result.append(arr[i])
    return result
```

### O(n²) - Quadratic Space

```python
def create_matrix(n):
    """Creates an n×n matrix"""
    return [[0] * n for _ in range(n)]
```

## Practical Examples

### Example 1: Two Sum Problem

**Brute Force Approach:**
```python
def two_sum_brute_force(nums, target):
    """
    Time: O(n²) - nested loops
    Space: O(1) - only using a few variables
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None
```

**Hash/Dictionary Approach:**
```python
def two_sum_dictionary(nums, target):
    """
    Time: O(n) - single pass through array/list
    Space: O(n) - storing numbers in hash/dictionary
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None
```

**Trade-off**: Hash/dictionary uses more space but is much faster!

### Example 2: Finding Duplicates

**Approach 1: Nested Loops**
```python
def has_duplicate_brute(nums):
    """
    Time: O(n²)
    Space: O(1)
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
```

**Approach 2: Sorting**
```python
def has_duplicate_sort(nums):
    """
    Time: O(n log n) - sorting
    Space: O(1) - if sorting in-place
    """
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False
```

**Approach 3: Set**
```python
def has_duplicate_set(nums):
    """
    Time: O(n) - single pass
    Space: O(n) - storing in set
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

## Choosing the Right Approach

Consider:
1. **Input size**: Small inputs might not need optimization
2. **Time vs Space**: Can you trade space for time?
3. **Constraints**: What are the problem constraints?
4. **Readability**: Sometimes simpler code is better

## Practice Problems

### Problem 1: Analyze Complexity
What's the time and space complexity of this function?

```python
def mystery_function(arr):
    result = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                result.append((i, j))
    return result
```

### Problem 2: Optimize This Function
This function finds all pairs that sum to target. Can you improve its complexity?

```python
def find_pairs_brute(arr, target):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs
```

### Problem 3: Compare Approaches
Implement three different ways to find if an array/list contains a target value, and analyze their complexities.

## Practice Time!

**Great work!** You've reached the practice exercises.

Try to solve the problems above on your own before checking solutions.
When you're ready, you can:
- Check the solutions in the original markdown file
- Ask your instructor for help
- Discuss with classmates

Remember: The process of solving is more important than getting the answer immediately!

## Key Takeaways

1. **Big O describes worst-case performance** - Focus on how algorithms scale
2. **Common complexities**: O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)
3. **Time vs Space trade-offs** - Often you can use more space for better time
4. **Analyze before optimizing** - Make sure optimization is needed
5. **Constants don't matter** - O(2n) = O(n), focus on growth rate

## Complexity Cheat Sheet

| Operation | Time Complexity | Notes |
|-----------|----------------|-------|
| Array/list access | O(1) | Direct indexing |
| Array/list search | O(n) | Must check each element |
| Hash/dictionary lookup | O(1) | Average case |
| Hash/dictionary insert | O(1) | Average case |
| Binary search | O(log n) | Requires sorted array/list |
| Merge sort | O(n log n) | Efficient sorting |
| Bubble sort | O(n²) | Simple but slow |
| Nested loops | O(n²) | Common pattern |

