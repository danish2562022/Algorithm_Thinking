# Tutorial 2: Problem-Solving Strategies

## Introduction

Effective problem-solving is the foundation of algorithmic thinking. This tutorial teaches you systematic approaches to tackle any computational problem, no matter how complex it initially seems.

## The Problem-Solving Framework

### Step 1: Understand the Problem

Before writing any code, make sure you fully understand what's being asked.

**Questions to ask:**
- What are the inputs and their formats?
- What is the expected output?
- What are the constraints? (size limits, time limits, etc.)
- Are there any edge cases?
- Can I restate the problem in my own words?

**Example Problem**: "Find two numbers in an array/list that add up to a target value."

**Understanding:**
- Input: Array/list of integers, target integer
- Output: Indices of two numbers that sum to target (or the numbers themselves)
- Constraints: Each number can only be used once
- Edge cases: No solution exists, duplicate numbers, negative numbers

### Step 2: Work Through Examples

Start with simple examples to build intuition.

```python
# Example 1: Simple case
numbers = [2, 7, 11, 15]
target = 9
# Answer: numbers[0] + numbers[1] = 2 + 7 = 9

# Example 2: Numbers not at start
numbers = [3, 2, 4]
target = 6
# Answer: numbers[1] + numbers[2] = 2 + 4 = 6

# Example 3: No solution
numbers = [1, 2, 3]
target = 10
# Answer: No solution exists
```

### Step 3: Break Down the Problem

Divide complex problems into smaller, manageable pieces.

**For the two-sum problem:**
1. For each number in the array/list
2. Check if there's another number that, when added, equals the target
3. Return the indices when found

### Step 4: Consider Multiple Approaches

Always think of multiple ways to solve a problem, then choose the best one.

**Approach 1: Brute Force**
```python
def two_sum_brute_force(numbers, target):
    """
    Check every pair of numbers.
    Time: O(n²) - nested loops
    Space: O(1) - only using a few variables
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]
    return None  # No solution found
```

**Approach 2: Using Hash/Dictionary**
```python
def two_sum_dictionary(numbers, target):
    """
    Use a hash/dictionary to store seen numbers.
    Time: O(n) - single pass through array/list
    Space: O(n) - storing numbers in hash/dictionary
    """
    seen = {}  # number -> index
    
    for i, num in enumerate(numbers):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
    
    return None  # No solution found
```

### Step 5: Write Pseudocode

Describe your algorithm in plain language before coding.

**Pseudocode for hash/dictionary approach:**
```
FUNCTION two_sum(numbers, target):
    CREATE empty hash/dictionary called seen
    
    FOR EACH index i and number num IN numbers:
        CALCULATE complement = target - num
        
        IF complement EXISTS IN seen:
            RETURN [seen[complement], i]
        
        STORE num -> i IN seen
    
    RETURN None (no solution found)
```

### Step 6: Implement and Test

```python
def two_sum(numbers, target):
    seen = {}
    
    for i, num in enumerate(numbers):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
    
    return None

# Test cases
test_cases = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([1, 2, 3], 10, None),
]

for numbers, target, expected in test_cases:
    result = two_sum(numbers, target)
    print(f"Input: {numbers}, Target: {target}")
    print(f"Result: {result}, Expected: {expected}")
    print(f"Match: {result == expected}\n")
```

## Common Problem-Solving Patterns

### Pattern 1: Two Pointers

Useful for problems involving sorted arrays/lists or palindromes.

**Example: Check if a string is a palindrome**
```python
def is_palindrome(s):
    """
    Use two pointers: one at start, one at end.
    Move them towards each other, comparing characters.
    """
    # Remove non-alphanumeric and convert to lowercase
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
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))  # False
```

### Pattern 2: Sliding Window

Useful for finding subarrays/sublists or substrings with specific properties.

**Example: Maximum sum of subarray/sublist of size k**
```python
def max_sum_sublist(numbers, k):
    """
    Use a sliding window of size k.
    Slide it across the array/list, keeping track of maximum sum.
    """
    if len(numbers) < k:
        return None
    
    # Calculate sum of first window
    window_sum = sum(numbers[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(numbers)):
        # Remove leftmost element, add rightmost element
        window_sum = window_sum - numbers[i - k] + numbers[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Test
numbers = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(f"Maximum sum of sublist of size {k}: {max_sum_sublist(numbers, k)}")
# Output: 39 (from [4, 2, 10, 23])
```

### Pattern 3: Hash/Dictionary for Lookups

Useful when you need fast lookups or counting.

**Example: Find the first non-repeating character**
```python
def first_non_repeating_char(s):
    """
    Count frequency of each character, then find first with count 1.
    """
    char_count = {}
    
    # Count frequencies
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find first character with count 1
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None  # All characters repeat

# Test
print(first_non_repeating_char("leetcode"))  # 'l'
print(first_non_repeating_char("loveleetcode"))  # 'v'
print(first_non_repeating_char("aabb"))  # None
```

## Problem-Solving Checklist

Use this checklist for every problem:

- [ ] **Understand**: Can I explain the problem in my own words?
- [ ] **Examples**: Have I worked through 2-3 examples manually?
- [ ] **Edge Cases**: What are the edge cases? (empty input, single element, etc.)
- [ ] **Approach**: What's my strategy? Can I think of alternatives?
- [ ] **Complexity**: What's the time and space complexity?
- [ ] **Pseudocode**: Can I write the steps in plain language?
- [ ] **Implement**: Write clean, readable code
- [ ] **Test**: Test with normal cases, edge cases, and boundary values
- [ ] **Optimize**: Can I improve the solution?

## Practice Problems

### Problem 1: Valid Anagram
Given two strings, determine if one is an anagram of the other.

**Example:**
- Input: s1 = "listen", s2 = "silent"
- Output: True

**Hint**: What makes two strings anagrams? How can you check this efficiently?

### Problem 2: Contains Duplicate
Given an array/list of integers, return True if any value appears at least twice.

**Example:**
- Input: [1, 2, 3, 1]
- Output: True

### Problem 3: Best Time to Buy and Sell Stock
You are given an array/list where prices[i] is the price of a stock on day i. You want to maximize profit by choosing a single day to buy and a different day to sell. Return the maximum profit.

**Example:**
- Input: [7, 1, 5, 3, 6, 4]
- Output: 5 (buy at 1, sell at 6)

**Hint**: Think about tracking the minimum price seen so far.

## Practice Time!

**Great work!** You've reached the practice exercises.

Try to solve the problems above on your own before checking solutions.
When you're ready, you can:
- Check the solutions in the original markdown file
- Ask your instructor for help
- Discuss with classmates

Remember: The process of solving is more important than getting the answer immediately!

## Key Takeaways

1. **Always understand before coding** - Spend time understanding the problem
2. **Work through examples** - Build intuition with concrete cases
3. **Break problems down** - Complex problems are just simple problems combined
4. **Consider multiple approaches** - There's usually more than one way to solve a problem
5. **Use patterns** - Recognize common patterns and adapt them
6. **Test thoroughly** - Edge cases often reveal bugs

## Next Steps

In the next tutorial, we'll learn about time and space complexity - how to analyze and compare the efficiency of different algorithms.
