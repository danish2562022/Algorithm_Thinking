# Tutorial 6: Data Structures for Algorithms

## Introduction

Choosing the right data structure is crucial for writing efficient algorithms. This tutorial covers essential data structures and when to use them.

## Arrays/Lists

### Characteristics

- **Access**: O(1) by index
- **Search**: O(n) for unsorted, O(log n) for sorted (binary search)
- **Insert/Delete**: O(n) at arbitrary position, O(1) at end
- **Space**: O(n)

### When to Use

- Need indexed access
- Sequential processing
- Fixed or known size

### Example: Two Sum with Sorted Array/List

```python
def two_sum_sorted(arr, target):
    """
    Use sorted array/list with two pointers
    Time: O(n log n) to sort + O(n) to find = O(n log n)
    Space: O(1)
    """
    arr.sort()
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None
```

## Hash Tables/Dictionaries

### Characteristics

- **Access**: O(1) average case
- **Search**: O(1) average case
- **Insert/Delete**: O(1) average case
- **Space**: O(n)

### When to Use

- Need fast lookups
- Counting frequencies
- Storing key-value pairs
- Removing duplicates

### Example: Frequency Counter

```python
def count_frequencies(arr):
    """
    Count frequency of each element
    Time: O(n)
    Space: O(n)
    """
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq

# Test
arr = [1, 2, 2, 3, 3, 3, 4]
print(count_frequencies(arr))
# Output: {1: 1, 2: 2, 3: 3, 4: 1}
```

### Example: Two Sum with Hash/Dictionary

```python
def two_sum_dictionary(arr, target):
    """
    Use hash/dictionary for O(1) lookups
    Time: O(n)
    Space: O(n)
    """
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None
```

## Sets

### Characteristics

- **Search**: O(1) average case
- **Insert/Delete**: O(1) average case
- **No duplicates**: Automatically handles uniqueness
- **Space**: O(n)

### When to Use

- Need to check membership quickly
- Removing duplicates
- Set operations (union, intersection)

### Example: Contains Duplicate

```python
def has_duplicate(arr):
    """
    Use set to track seen elements
    Time: O(n)
    Space: O(n)
    """
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

# Pythonic version
def has_duplicate_v2(arr):
    return len(arr) != len(set(arr))
```

## Stacks

### Characteristics

- **LIFO**: Last In, First Out
- **Operations**: Push O(1), Pop O(1), Peek O(1)
- **Space**: O(n)

### When to Use

- Matching parentheses
- Expression evaluation
- Undo/redo operations
- Depth-first search

### Example: Valid Parentheses

```python
def is_valid_parentheses(s):
    """
    Use stack to match opening and closing brackets
    Time: O(n)
    Space: O(n)
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            # Closing bracket
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            # Opening bracket
            stack.append(char)
    
    return len(stack) == 0

# Test
print(is_valid_parentheses("()[]{}"))  # True
print(is_valid_parentheses("([)]"))  # False
```

### Example: Next Greater Element

```python
def next_greater_element(nums):
    """
    Find next greater element for each element
    Use stack to maintain decreasing order
    Time: O(n)
    Space: O(n)
    """
    result = [-1] * len(nums)
    stack = []  # Store indices
    
    for i in range(len(nums)):
        # While current element is greater than stack top
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    
    return result

# Test
print(next_greater_element([4, 5, 2, 10]))  # [5, 10, 10, -1]
```

## Queues

### Characteristics

- **FIFO**: First In, First Out
- **Operations**: Enqueue O(1), Dequeue O(1)
- **Space**: O(n)

### When to Use

- Breadth-first search
- Level-order traversal
- Task scheduling
- Any FIFO requirement

### Example: Level-Order Traversal

```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root):
    """
    Use queue for BFS
    Time: O(n)
    Space: O(n)
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

## Heaps (Priority Queues)

### Characteristics

- **Min/Max element**: O(1) access
- **Insert**: O(log n)
- **Extract min/max**: O(log n)
- **Space**: O(n)

### When to Use

- Finding k largest/smallest elements
- Merging sorted lists
- Dijkstra's algorithm
- Any priority-based processing

### Example: Find K Largest Elements

```python
import heapq

def find_k_largest(nums, k):
    """
    Use min heap of size k
    Time: O(n log k)
    Space: O(k)
    """
    # Min heap (Python's heapq is min heap)
    heap = []
    
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)
    
    return sorted(heap, reverse=True)

# Test
nums = [3, 1, 4, 1, 5, 9, 2, 6]
k = 3
print(f"Top {k} largest: {find_k_largest(nums, k)}")  # [9, 6, 5]
```

### Example: Merge K Sorted Lists

```python
def merge_k_lists(lists):
    """
    Use min heap to merge k sorted lists
    Time: O(n log k) where n is total elements
    Space: O(k)
    """
    import heapq
    
    heap = []
    result = []
    
    # Initialize heap with first element of each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    
    # Merge
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        # Add next element from same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
    
    return result

# Test
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
print(merge_k_lists(lists))  # [1, 1, 2, 3, 4, 4, 5, 6]
```

## Trees

### Binary Search Tree (BST)

**Characteristics:**
- **Search**: O(log n) average, O(n) worst
- **Insert/Delete**: O(log n) average, O(n) worst
- **In-order traversal**: O(n) gives sorted order

**When to Use:**
- Need sorted order with dynamic updates
- Range queries
- Finding predecessor/successor

### Example: BST Operations

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def search_bst(root, val):
    """
    Search in BST
    Time: O(log n) average, O(n) worst
    """
    if not root or root.val == val:
        return root
    
    if val < root.val:
        return search_bst(root.left, val)
    else:
        return search_bst(root.right, val)

def insert_bst(root, val):
    """
    Insert into BST
    Time: O(log n) average, O(n) worst
    """
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    
    return root
```

## Graphs

### Representation: Adjacency List

```python
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        # For undirected graph, also add:
        # self.graph[v].append(u)
    
    def dfs(self, start, visited=None):
        """
        Depth-First Search using recursion (stack)
        Time: O(V + E)
        Space: O(V)
        """
        if visited is None:
            visited = set()
        
        visited.add(start)
        print(start, end=' ')
        
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
    
    def bfs(self, start):
        """
        Breadth-First Search using queue
        Time: O(V + E)
        Space: O(V)
        """
        from collections import deque
        
        visited = set()
        queue = deque([start])
        visited.add(start)
        
        while queue:
            node = queue.popleft()
            print(node, end=' ')
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Test
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("DFS:", end=' ')
g.dfs(2)  # 2 0 1 3
print("\nBFS:", end=' ')
g.bfs(2)  # 2 0 3 1
```

## Choosing the Right Data Structure

### Decision Guide

| Need | Data Structure | Reason |
|------|---------------|--------|
| Fast lookup by key | Hash/Dictionary | O(1) average |
| Sorted order | BST / Sorted Array/List | Maintains order |
| Check membership | Set | O(1) average |
| LIFO operations | Stack | Natural for LIFO |
| FIFO operations | Queue | Natural for FIFO |
| Priority processing | Heap | O(log n) insert/extract |
| Relationships | Graph | Models connections |
| Sequential access | Array/List | Simple and efficient |

### Example: Problem Analysis

**Problem**: Find first non-repeating character in string.

**Analysis:**
- Need to count frequencies → Use hash/dictionary
- Need to maintain order → Use ordered dict or two passes
- Need fast lookup → Hash/dictionary is perfect

```python
def first_non_repeating_char(s):
    """
    Use hash/dictionary to count, then find first with count 1
    Time: O(n)
    Space: O(n)
    """
    char_count = {}
    
    # Count frequencies
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find first non-repeating
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None
```

## Practice Problems

### Problem 1: Implement Stack using Queues
Implement a stack using only queue operations.

### Problem 2: LRU Cache
Design a data structure that follows Least Recently Used (LRU) cache policy.

### Problem 3: Design Twitter Feed
Design a simplified Twitter feed that shows recent tweets from users you follow.

## Practice Time!

**Great work!** You've reached the practice exercises.

Try to solve the problems above on your own before checking solutions.
When you're ready, you can:
- Check the solutions in the original markdown file
- Ask your instructor for help
- Discuss with classmates

Remember: The process of solving is more important than getting the answer immediately!

## Key Takeaways

1. **Choose based on operations needed**: What operations do you need most?
2. **Consider time complexity**: Different structures have different costs
3. **Consider space complexity**: Some structures use more memory
4. **Combine structures**: Complex problems may need multiple structures
5. **Python built-ins**: Use `collections` module for advanced structures

## Data Structure Complexity Cheat Sheet

| Structure | Access | Search | Insert | Delete | Space |
|-----------|--------|--------|--------|--------|-------|
| Array/List | O(1) | O(n) | O(n) | O(n) | O(n) |
| Hash/Dictionary | O(1) | O(1) | O(1) | O(1) | O(n) |
| Set | N/A | O(1) | O(1) | O(1) | O(n) |
| Stack | O(1)* | N/A | O(1) | O(1) | O(n) |
| Queue | O(1)* | N/A | O(1) | O(1) | O(n) |
| Heap | O(1)** | N/A | O(log n) | O(log n) | O(n) |
| BST | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |

*Top/front element only  
**Min/max element only

## Next Steps

In the final tutorial, we'll work through complete problem-solving walkthroughs, applying all the concepts we've learned!
