# Tutorial 4: Common Algorithmic Patterns

## Introduction

Many problems share similar structures. Recognizing these patterns helps you solve new problems more efficiently. This tutorial covers four essential algorithmic patterns.

## Pattern 1: Divide and Conquer

**Strategy**: Break a problem into smaller subproblems, solve them recursively, and combine the results.

### Key Characteristics

- Problem can be divided into similar subproblems
- Subproblems are independent
- Solutions can be combined efficiently

### Classic Example: Merge Sort

```python
def merge_sort(arr):
    """
    Divide: Split array/list in half
    Conquer: Sort each half recursively
    Combine: Merge the sorted halves
    Time: O(n log n)
    """
    # Base case: array/list of 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr
    
    # Divide: split into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Combine: merge the sorted halves
    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays/lists into one sorted array/list"""
    result = []
    i = j = 0
    
    # Compare elements and add smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Test
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(f"Original: {arr}")
print(f"Sorted: {sorted_arr}")
```

### Example: Finding Maximum Element

```python
def find_max_divide_conquer(arr, left, right):
    """
    Divide: Split array/list in half
    Conquer: Find max in each half
    Combine: Return the larger of the two
    Time: O(n) - still need to check all elements
    """
    # Base case: single element
    if left == right:
        return arr[left]
    
    # Divide
    mid = (left + right) // 2
    
    # Conquer
    max_left = find_max_divide_conquer(arr, left, mid)
    max_right = find_max_divide_conquer(arr, mid + 1, right)
    
    # Combine
    return max(max_left, max_right)

# Wrapper function
def find_max(arr):
    if not arr:
        return None
    return find_max_divide_conquer(arr, 0, len(arr) - 1)

# Test
print(find_max([3, 7, 2, 9, 1]))  # 9
```

### When to Use Divide and Conquer

- Problem can be broken into similar subproblems
- Subproblems can be solved independently
- Combining solutions is efficient
- Examples: Sorting, binary search, finding max/min, matrix multiplication

## Pattern 2: Greedy Algorithms

**Strategy**: Make the locally optimal choice at each step, hoping it leads to a global optimum.

### Key Characteristics

- Makes best choice at each step
- Doesn't reconsider previous choices
- Often efficient but may not always give optimal solution

### Example: Activity Selection Problem

**Problem**: Given activities with start and end times, select maximum number of non-overlapping activities.

```python
def activity_selection(activities):
    """
    Greedy strategy: Always pick the activity that ends earliest
    Time: O(n log n) - sorting
    """
    # Sort by end time
    activities.sort(key=lambda x: x[1])
    
    selected = [activities[0]]  # Always select first activity
    
    for activity in activities[1:]:
        # If this activity starts after last selected ends, select it
        if activity[0] >= selected[-1][1]:
            selected.append(activity)
    
    return selected

# Test
# Format: (start_time, end_time)
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
selected = activity_selection(activities)
print(f"Selected activities: {selected}")
print(f"Total: {len(selected)} activities")
```

### Example: Minimum Coins Problem

**Problem**: Find minimum number of coins needed to make a given amount (assuming unlimited coins).

```python
def min_coins_greedy(amount, coins):
    """
    Greedy: Always use largest coin possible
    Note: This works for standard coin systems but may fail for arbitrary coins
    Time: O(amount / min_coin)
    """
    coins.sort(reverse=True)  # Start with largest coins
    result = []
    remaining = amount
    
    for coin in coins:
        count = remaining // coin
        if count > 0:
            result.extend([coin] * count)
            remaining %= coin
    
    return result if remaining == 0 else None

# Test
coins = [1, 5, 10, 25]
amount = 67
result = min_coins_greedy(amount, coins)
print(f"Amount: {amount} cents")
print(f"Coins needed: {result}")
print(f"Total coins: {len(result)}")
```

**Note**: Greedy doesn't always work! For coins = [1, 3, 4] and amount = 6:
- Greedy: [4, 1, 1] = 3 coins
- Optimal: [3, 3] = 2 coins

### When to Use Greedy

- Problem has optimal substructure
- Greedy choice leads to optimal solution
- Examples: Activity selection, minimum spanning tree, shortest path (Dijkstra's)

## Pattern 3: Two Pointers

**Strategy**: Use two pointers moving through data structure, often from different ends or at different speeds.

### Example: Two Sum in Sorted Array/List

```python
def two_sum_sorted(arr, target):
    """
    Use two pointers: one at start, one at end
    Move them based on sum comparison
    Time: O(n)
    Space: O(1)
    """
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum
    
    return None  # No solution

# Test
arr = [2, 7, 11, 15]
target = 9
print(two_sum_sorted(arr, target))  # [0, 1]
```

### Example: Remove Duplicates from Sorted Array/List

```python
def remove_duplicates(arr):
    """
    Use two pointers: one for reading, one for writing
    Time: O(n)
    Space: O(1) - modifying in place
    """
    if not arr:
        return 0
    
    write_index = 1  # Position to write next unique element
    
    for read_index in range(1, len(arr)):
        # If current element is different from previous, it's unique
        if arr[read_index] != arr[read_index - 1]:
            arr[write_index] = arr[read_index]
            write_index += 1
    
    return write_index  # Length of unique elements

# Test
arr = [1, 1, 2, 2, 2, 3, 4, 4, 5]
length = remove_duplicates(arr)
print(f"Unique elements: {arr[:length]}")
print(f"Length: {length}")
```

### Example: Palindrome Check

```python
def is_palindrome(s):
    """
    Two pointers from both ends moving towards center
    Time: O(n)
    Space: O(1)
    """
    # Clean string: remove non-alphanumeric and lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    
    left = 0
    right = len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Test
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("race a car"))  # False
```

### When to Use Two Pointers

- Working with sorted arrays/lists
- Need to find pairs or triplets
- Removing duplicates
- Checking palindromes
- Often reduces O(n²) to O(n)

## Pattern 4: Sliding Window

**Strategy**: Maintain a window of elements and slide it across the data structure.

### Example: Maximum Sum Sublist of Size K

```python
def max_sum_sublist(arr, k):
    """
    Maintain a window of size k, slide it across array/list
    Time: O(n)
    Space: O(1)
    """
    if len(arr) < k:
        return None
    
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(arr)):
        # Remove leftmost element, add rightmost element
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Test
arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(f"Maximum sum of subarray of size {k}: {max_sum_subarray(arr, k)}")
```

### Example: Longest Substring Without Repeating Characters

```python
def longest_unique_substring(s):
    """
    Use sliding window with set to track characters
    Time: O(n)
    Space: O(min(n, m)) where m is charset size
    """
    if not s:
        return 0
    
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # If character already in window, shrink from left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Test
print(longest_unique_substring("abcabcbb"))  # 3 ("abc")
print(longest_unique_substring("bbbbb"))  # 1 ("b")
print(longest_unique_substring("pwwkew"))  # 3 ("wke")
```

### Example: Minimum Window Substring

```python
def min_window_substring(s, t):
    """
    Find minimum window in s that contains all characters of t
    Time: O(|s| + |t|)
    Space: O(|s| + |t|)
    """
    if not s or not t or len(s) < len(t):
        return ""
    
    # Count characters needed
    need = {}
    for char in t:
        need[char] = need.get(char, 0) + 1
    
    # Sliding window
    left = 0
    have = {}
    min_len = float('inf')
    min_window = ""
    required = len(need)
    formed = 0
    
    for right in range(len(s)):
        char = s[right]
        have[char] = have.get(char, 0) + 1
        
        # Check if current character completes a requirement
        if char in need and have[char] == need[char]:
            formed += 1
        
        # Try to shrink window from left
        while left <= right and formed == required:
            # Update minimum window
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = s[left:right + 1]
            
            # Remove leftmost character
            left_char = s[left]
            have[left_char] -= 1
            if left_char in need and have[left_char] < need[left_char]:
                formed -= 1
            
            left += 1
    
    return min_window

# Test
print(min_window_substring("ADOBECODEBANC", "ABC"))  # "BANC"
```

### When to Use Sliding Window

- Finding subarrays/sublists or substrings with specific properties
- Problems involving consecutive elements
- Often converts O(n²) or O(n³) to O(n)

## Pattern Comparison

| Pattern | Best For | Time Complexity | Key Insight |
|---------|----------|----------------|-------------|
| Divide & Conquer | Problems that can be split | Often O(n log n) | Recursive structure |
| Greedy | Optimization with local choices | Often O(n log n) | Local optimum = global |
| Two Pointers | Sorted arrays, pairs | O(n) | Move pointers based on condition |
| Sliding Window | Subarrays/sublists or substrings | O(n) | Maintain window state |

## Practice Problems

### Problem 1: Implement Binary Search
Use divide and conquer to implement binary search.

### Problem 2: Container With Most Water
Given array/list of heights, find two lines that form container with most water. Use two pointers.

### Problem 3: Longest Repeating Character Replacement
Given string and integer k, find longest substring with same character after replacing at most k characters. Use sliding window.

## Practice Time!

**Great work!** You've reached the practice exercises.

Try to solve the problems above on your own before checking solutions.
When you're ready, you can:
- Check the solutions in the original markdown file
- Ask your instructor for help
- Discuss with classmates

Remember: The process of solving is more important than getting the answer immediately!

## Key Takeaways

1. **Recognize patterns** - Many problems share similar structures
2. **Choose the right pattern** - Match pattern to problem characteristics
3. **Practice** - The more problems you solve, the better you recognize patterns
4. **Combine patterns** - Complex problems may use multiple patterns

## Next Steps

In the next tutorial, we'll explore Dynamic Programming - a powerful technique for solving optimization problems with overlapping subproblems.
