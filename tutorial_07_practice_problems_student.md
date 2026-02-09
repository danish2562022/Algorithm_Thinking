# Tutorial 7: Practice Problems and Solutions

## Introduction

This tutorial provides complete walkthroughs of challenging problems, demonstrating how to apply all the concepts we've learned. We'll solve problems step-by-step, consider multiple approaches, and discuss common pitfalls.

## Problem 1: Group Anagrams

**Problem**: Given an array/list of strings, group anagrams together.

**Example:**
```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

### Step 1: Understand the Problem

- **Input**: Array/list of strings
- **Output**: Groups of anagrams
- **Key insight**: Anagrams have the same character frequencies
- **Edge cases**: Empty array/list, single string, no anagrams

### Step 2: Approach

**Approach 1: Sort each string**
- Sort characters in each string
- Use sorted string as key in hash/dictionary
- Group strings with same sorted key

**Approach 2: Count characters**
- Count frequency of each character
- Use frequency tuple as key
- Group strings with same frequency

### Step 3: Implement

```python
def group_anagrams(strs):
    """
    Approach 1: Sort each string
    Time: O(n * k log k) where n is strings, k is avg length
    Space: O(n * k)
    """
    groups = {}
    
    for s in strs:
        # Sort string to get canonical form
        key = ''.join(sorted(s))
        
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    
    return list(groups.values())

# Test
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(strs)
print(result)
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

**Alternative using character counts:**

```python
def group_anagrams_v2(strs):
    """
    Approach 2: Count characters
    Time: O(n * k) where k is avg length
    Space: O(n * k)
    """
    from collections import defaultdict
    
    groups = defaultdict(list)
    
    for s in strs:
        # Count characters
        count = [0] * 26  # Assuming lowercase letters
        for char in s:
            count[ord(char) - ord('a')] += 1
        
        # Use tuple as key
        groups[tuple(count)].append(s)
    
    return list(groups.values())
```

### Step 4: Analysis

- **Time Complexity**: O(n * k log k) for sorting approach, O(n * k) for counting
- **Space Complexity**: O(n * k) for both
- **Best approach**: Counting is faster for longer strings

## Problem 2: Longest Consecutive Sequence

**Problem**: Given unsorted array/list of integers, find length of longest consecutive sequence.

**Example:**
```
Input: [100, 4, 200, 1, 3, 2]
Output: 4 (sequence is 1, 2, 3, 4)
```

### Step 1: Understand

- **Input**: Unsorted array/list
- **Output**: Length of longest consecutive sequence
- **Constraint**: O(n) time complexity
- **Edge cases**: Empty array/list, single element, duplicates

### Step 2: Approach

**Brute Force**: Sort and find longest sequence → O(n log n)

**Optimal**: Use set for O(1) lookups
- Convert array/list to set
- For each number, check if it's start of sequence (num-1 not in set)
- Expand sequence while num+1 exists
- Track maximum length

### Step 3: Implement

```python
def longest_consecutive(nums):
    """
    Use set for O(1) lookups
    Time: O(n) - each number visited at most twice
    Space: O(n)
    """
    if not nums:
        return 0
    
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        # Only start sequence if num is the start (num-1 not in set)
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            # Expand sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length

# Test
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))  # 4
```

### Step 4: Why This Works

- Each number is visited at most twice (once in outer loop, once when expanding)
- Starting only from sequence starts avoids redundant work
- Set gives O(1) lookups

## Problem 3: Product of List Except Self

**Problem**: Given array/list nums, return array/list where answer[i] is product of all elements except nums[i]. Must be O(n) time and O(1) extra space (excluding output array/list).

**Example:**
```
Input: [1, 2, 3, 4]
Output: [24, 12, 8, 6]
```

### Step 1: Understand

- **Constraint**: Cannot use division
- **Constraint**: O(n) time, O(1) extra space
- **Edge cases**: Zeros, negative numbers

### Step 2: Approach

**Idea**: 
- For each position i, need product of all elements before i and after i
- Two passes:
  1. Left pass: Calculate product of all elements to the left
  2. Right pass: Multiply by product of all elements to the right

### Step 3: Implement

```python
def product_except_self(nums):
    """
    Two passes: left products, then right products
    Time: O(n)
    Space: O(1) excluding output array/list
    """
    n = len(nums)
    result = [1] * n
    
    # Left pass: result[i] = product of all elements to the left
    for i in range(1, n):
        result[i] = result[i - 1] * nums[i - 1]
    
    # Right pass: multiply by product of all elements to the right
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result

# Test
nums = [1, 2, 3, 4]
print(product_except_self(nums))  # [24, 12, 8, 6]
```

### Step 4: Walkthrough

```
nums = [1, 2, 3, 4]

After left pass:
result = [1, 1, 2, 6]
         (1, 1*1, 1*1*2, 1*1*2*3)

After right pass (multiplying by right products):
i=3: result[3] = 6 * 1 = 6, right_product = 4
i=2: result[2] = 2 * 4 = 8, right_product = 12
i=1: result[1] = 1 * 12 = 12, right_product = 24
i=0: result[0] = 1 * 24 = 24, right_product = 24

Final: [24, 12, 8, 6]
```

## Problem 4: Word Ladder

**Problem**: Given two words and a dictionary, find length of shortest transformation sequence from beginWord to endWord, changing one letter at a time.

**Example:**
```
beginWord = "hit", endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
Output: 5 ("hit" -> "hot" -> "dot" -> "dog" -> "cog")
```

### Step 1: Understand

- **Graph problem**: Words are nodes, one-letter differences are edges
- **Shortest path**: Use BFS
- **Edge cases**: endWord not in list, no path exists

### Step 2: Approach

**BFS Strategy:**
1. Start from beginWord
2. Generate all words that differ by one letter
3. Use BFS to find shortest path to endWord
4. Track level/distance

### Step 3: Implement

```python
from collections import deque

def ladder_length(beginWord, endWord, wordList):
    """
    BFS to find shortest transformation sequence
    Time: O(M * N) where M is word length, N is wordList size
    Space: O(N)
    """
    word_set = set(wordList)
    
    if endWord not in word_set:
        return 0
    
    queue = deque([(beginWord, 1)])  # (word, level)
    visited = {beginWord}
    
    while queue:
        word, level = queue.popleft()
        
        if word == endWord:
            return level
        
        # Generate all words that differ by one letter
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char == word[i]:
                    continue
                
                new_word = word[:i] + char + word[i + 1:]
                
                if new_word in word_set and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, level + 1))
    
    return 0  # No path found

# Test
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(ladder_length(beginWord, endWord, wordList))  # 5
```

## Problem 5: Merge Intervals

**Problem**: Given array/list of intervals, merge all overlapping intervals.

**Example:**
```
Input: [[1,3], [2,6], [8,10], [15,18]]
Output: [[1,6], [8,10], [15,18]]
```

### Step 1: Understand

- **Overlap**: Intervals overlap if start <= previous end
- **Strategy**: Sort by start time, then merge
- **Edge cases**: Empty array/list, no overlaps, all overlap

### Step 2: Approach

1. Sort intervals by start time
2. Iterate through sorted intervals
3. If current overlaps with last merged, merge them
4. Otherwise, add as new interval

### Step 3: Implement

```python
def merge_intervals(intervals):
    """
    Sort and merge overlapping intervals
    Time: O(n log n) - sorting
    Space: O(n) - result array/list
    """
    if not intervals:
        return []
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        
        # Check if current overlaps with last merged interval
        if current[0] <= last[1]:
            # Merge: update end time
            last[1] = max(last[1], current[1])
        else:
            # No overlap, add as new interval
            merged.append(current)
    
    return merged

# Test
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))  # [[1, 6], [8, 10], [15, 18]]
```

## Common Pitfalls and How to Avoid Them

### Pitfall 1: Off-by-One Errors

**Problem**: Incorrect array/list indices

**Solution**: 
- Use `range(len(arr))` carefully
- Check boundary conditions
- Test with edge cases (empty, single element)

### Pitfall 2: Modifying Collections While Iterating

**Problem**: 
```python
# WRONG
for item in my_list:
    if condition(item):
        my_list.remove(item)  # Modifies list during iteration!
```

**Solution**: 
```python
# RIGHT: Create new list or iterate backwards
my_list = [item for item in my_list if not condition(item)]
```

### Pitfall 3: Not Handling Edge Cases

**Problem**: Code fails on empty input, single element, etc.

**Solution**: Always test:
- Empty input
- Single element
- Two elements
- All same elements
- Boundary values

### Pitfall 4: Incorrect Complexity Analysis

**Problem**: Claiming O(n) but using O(n log n) operations

**Solution**: 
- Count nested loops
- Check for sorting operations
- Consider all operations, not just main loop

### Pitfall 5: Not Considering Space Complexity

**Problem**: Using extra space unnecessarily

**Solution**: 
- Can you solve in-place?
- Do you need to store all intermediate results?
- Can you use a more space-efficient data structure?

## Problem-Solving Template

Use this template for any problem:

```python
def solve_problem(input_data):
    """
    1. Understand: What are we solving?
    2. Edge cases: Handle empty, single element, etc.
    3. Approach: What's the strategy?
    4. Implement: Write clean code
    5. Test: Verify with examples
    """
    
    # Handle edge cases
    if not input_data:
        return None  # or appropriate default
    
    # Main algorithm
    # ... your solution ...
    
    return result
```

## Additional Practice Problems

### Problem 6: Valid Sudoku
Determine if a 9×9 Sudoku board is valid.

**Hint**: Use sets to track seen numbers in rows, columns, and boxes.

### Problem 7: Course Schedule
Given courses and prerequisites, determine if you can finish all courses.

**Hint**: Detect cycles in directed graph (topological sort).

### Problem 8: Kth Largest Element
Find kth largest element in unsorted array/list.

**Hint**: Use heap or quickselect algorithm.

## Practice Time!

**Great work!** You've reached the practice exercises.

Try to solve the problems above on your own before checking solutions.
When you're ready, you can:
- Check the solutions in the original markdown file
- Ask your instructor for help
- Discuss with classmates

Remember: The process of solving is more important than getting the answer immediately!

## Key Takeaways

1. **Read carefully**: Understand constraints and requirements
2. **Start simple**: Begin with brute force, then optimize
3. **Think about data structures**: Choose the right tool for the job
4. **Handle edge cases**: Always test boundary conditions
5. **Analyze complexity**: Know your algorithm's performance
6. **Practice regularly**: The more problems you solve, the better you get

## Final Tips for Success

1. **Consistency**: Practice daily, even if just one problem
2. **Review**: Revisit problems you struggled with
3. **Explain**: Try explaining solutions to others (or yourself)
4. **Pattern recognition**: Look for similarities between problems
5. **Don't give up**: Struggling is part of learning!

## Conclusion

Congratulations on completing the Algorithmic Thinking tutorial series! You now have:

- Understanding of what algorithms are and how to think algorithmically
- Problem-solving strategies and frameworks
- Knowledge of time and space complexity
- Familiarity with common algorithmic patterns
- Understanding of dynamic programming
- Knowledge of data structures and when to use them
- Practice solving real problems

Keep practicing, stay curious, and remember: every expert was once a beginner. Happy coding!
