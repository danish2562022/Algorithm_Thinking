# Tutorial 5: Dynamic Programming

## Introduction

Dynamic Programming (DP) is a powerful technique for solving optimization problems by breaking them into overlapping subproblems and storing results to avoid recomputation.

## What is Dynamic Programming?

**Key Idea**: Solve each subproblem only once and store the result for future use.

**When to Use DP:**
1. **Overlapping subproblems**: Same subproblems appear multiple times
2. **Optimal substructure**: Optimal solution contains optimal solutions to subproblems
3. **Memoization or Tabulation**: Store results to avoid recomputation

## The Fibonacci Problem

### Naive Recursive Approach

```python
def fibonacci_naive(n):
    """
    Naive recursive approach
    Time: O(2ⁿ) - exponential!
    Problem: Recalculates same values many times
    """
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)

# This is VERY slow for large n
# fibonacci_naive(40) takes a very long time
```

**Problem**: `fibonacci_naive(5)` calculates `fibonacci_naive(3)` multiple times!

### Memoization (Top-Down DP)

```python
def fibonacci_memo(n, memo=None):
    """
    Memoization: Store results as we compute them
    Time: O(n) - each value computed once
    Space: O(n) - memo dictionary + recursion stack
    """
    if memo is None:
        memo = {}
    
    # Base cases
    if n <= 1:
        return n
    
    # Check if already computed
    if n in memo:
        return memo[n]
    
    # Compute and store
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# Much faster!
print(fibonacci_memo(40))  # Fast!
```

### Tabulation (Bottom-Up DP)

```python
def fibonacci_tab(n):
    """
    Tabulation: Build solution from bottom up
    Time: O(n)
    Space: O(n) - array/list to store results
    """
    if n <= 1:
        return n
    
    # Table to store results
    dp = [0] * (n + 1)
    dp[1] = 1
    
    # Fill table bottom-up
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

# Even more efficient - no recursion overhead
print(fibonacci_tab(40))  # Very fast!
```

### Space-Optimized Version

```python
def fibonacci_optimized(n):
    """
    Only need last two values, not entire array/list
    Time: O(n)
    Space: O(1) - only storing two variables
    """
    if n <= 1:
        return n
    
    prev2 = 0  # F(0)
    prev1 = 1  # F(1)
    
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1

# Most space-efficient!
print(fibonacci_optimized(40))
```

## Classic DP Problems

### Problem 1: Climbing Stairs

**Problem**: You can climb 1 or 2 steps at a time. How many ways to reach the top?

```python
def climb_stairs(n):
    """
    Similar to Fibonacci!
    Ways to reach step n = ways to reach (n-1) + ways to reach (n-2)
    Time: O(n)
    Space: O(1)
    """
    if n <= 2:
        return n
    
    prev2 = 1  # Ways to reach step 1
    prev1 = 2  # Ways to reach step 2
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1

# Test
print(f"Ways to climb 5 steps: {climb_stairs(5)}")  # 8
```

### Problem 2: Coin Change

**Problem**: Find minimum number of coins needed to make amount.

```python
def coin_change(coins, amount):
    """
    DP: dp[i] = minimum coins to make amount i
    Time: O(amount * len(coins))
    Space: O(amount)
    """
    # dp[i] = minimum coins to make amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins needed for amount 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Test
coins = [1, 3, 4]
amount = 6
print(f"Minimum coins for {amount}: {coin_change(coins, amount)}")  # 2 (3+3)
```

### Problem 3: Longest Increasing Subsequence (LIS)

**Problem**: Find length of longest strictly increasing subsequence.

```python
def length_of_lis(nums):
    """
    DP: dp[i] = length of LIS ending at index i
    Time: O(n²)
    Space: O(n)
    """
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n  # Each element is a subsequence of length 1
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Test
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(f"Length of LIS: {length_of_lis(nums)}")  # 4 ([2, 3, 7, 18])
```

### Problem 4: House Robber

**Problem**: Rob houses to maximize money, but can't rob two adjacent houses.

```python
def rob(houses):
    """
    DP: At each house, decide to rob or skip
    dp[i] = max money robbing up to house i
    Time: O(n)
    Space: O(1) - optimized version
    """
    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]
    
    # Only need last two values
    prev2 = houses[0]  # Max money up to house 0
    prev1 = max(houses[0], houses[1])  # Max money up to house 1
    
    for i in range(2, len(houses)):
        # Either rob current house + best up to i-2, or skip and take best up to i-1
        current = max(prev1, prev2 + houses[i])
        prev2 = prev1
        prev1 = current
    
    return prev1

# Test
houses = [2, 7, 9, 3, 1]
print(f"Maximum money: {rob(houses)}")  # 12 (rob houses 0, 2, 4)
```

### Problem 5: Edit Distance (Levenshtein Distance)

**Problem**: Minimum operations to convert string1 to string2 (insert, delete, replace).

```python
def edit_distance(word1, word2):
    """
    DP: dp[i][j] = edit distance between word1[:i] and word2[:j]
    Time: O(m * n) where m, n are lengths
    Space: O(m * n)
    """
    m, n = len(word1), len(word2)
    
    # dp[i][j] = edit distance between word1[:i] and word2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases
    for i in range(m + 1):
        dp[i][0] = i  # Need i deletions
    for j in range(n + 1):
        dp[0][j] = j  # Need j insertions
    
    # Fill table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                # Characters match, no operation needed
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Try all three operations, take minimum
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Delete from word1
                    dp[i][j - 1],      # Insert into word1
                    dp[i - 1][j - 1]   # Replace
                )
    
    return dp[m][n]

# Test
print(edit_distance("horse", "ros"))  # 3
print(edit_distance("intention", "execution"))  # 5
```

## DP Patterns

### Pattern 1: 1D DP

Problems where state depends on one variable.

**Examples**: Fibonacci, Climbing Stairs, House Robber

```python
# General structure
def solve_1d_dp(n):
    dp = [0] * (n + 1)
    dp[0] = base_case
    
    for i in range(1, n + 1):
        dp[i] = compute(dp, i)
    
    return dp[n]
```

### Pattern 2: 2D DP

Problems where state depends on two variables.

**Examples**: Edit Distance, Longest Common Subsequence

```python
# General structure
def solve_2d_dp(m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = base_case_i
    for j in range(n + 1):
        dp[0][j] = base_case_j
    
    # Fill table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = compute(dp, i, j)
    
    return dp[m][n]
```

### Pattern 3: Knapsack Problems

**0/1 Knapsack**: Each item can be taken at most once.

```python
def knapsack_01(weights, values, capacity):
    """
    DP: dp[i][w] = max value using first i items with capacity w
    Time: O(n * capacity)
    Space: O(n * capacity)
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                # Can take item i: max of taking or not taking
                dp[i][w] = max(
                    dp[i - 1][w],  # Don't take
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]  # Take
                )
            else:
                # Can't take item i
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

# Test
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7
print(f"Maximum value: {knapsack_01(weights, values, capacity)}")  # 9
```

## Steps to Solve DP Problems

1. **Identify subproblems**: What are you trying to compute?
2. **Define state**: What does dp[i] or dp[i][j] represent?
3. **Find recurrence relation**: How do you compute current state from previous states?
4. **Base cases**: What are the smallest subproblems?
5. **Choose approach**: Memoization (top-down) or tabulation (bottom-up)?
6. **Optimize space**: Can you reduce space complexity?

## Practice Problems

### Problem 1: Unique Paths
A robot is at top-left of m×n grid. It can only move right or down. How many unique paths to bottom-right?

### Problem 2: Maximum Subarray/Sublist
Find the contiguous subarray/sublist with the largest sum (Kadane's algorithm).

### Problem 3: Decode Ways
A message containing letters A-Z can be encoded as: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a string of digits, count ways to decode it.

## Practice Time!

**Great work!** You've reached the practice exercises.

Try to solve the problems above on your own before checking solutions.
When you're ready, you can:
- Check the solutions in the original markdown file
- Ask your instructor for help
- Discuss with classmates

Remember: The process of solving is more important than getting the answer immediately!

## Key Takeaways

1. **Recognize DP problems**: Overlapping subproblems + optimal substructure
2. **Choose approach**: Memoization (recursive) or tabulation (iterative)
3. **Define state clearly**: What does dp[i] represent?
4. **Find recurrence**: How to compute current state from previous?
5. **Optimize space**: Often only need last few values, not entire array/list
6. **Practice**: DP requires pattern recognition - solve many problems!

## Common DP Patterns Summary

| Pattern | Example Problems | Key Insight |
|---------|-----------------|-------------|
| 1D DP | Fibonacci, Climbing Stairs | State depends on one variable |
| 2D DP | Edit Distance, LCS | State depends on two variables |
| Knapsack | 0/1 Knapsack, Coin Change | Optimization with constraints |
| Interval DP | Matrix Chain Multiplication | Work on intervals |
| Tree DP | Binary Tree Problems | Process tree bottom-up |

## Next Steps

In the next tutorial, we'll explore how different data structures can make algorithms more efficient and when to use each one.
