# Tutorial 1: Introduction to Algorithmic Thinking

## What is an Algorithm?

An **algorithm** is a step-by-step procedure or set of rules for solving a problem or completing a task. Think of it as a recipe - it tells you exactly what to do, in what order, to achieve a desired result.

### Key Characteristics of Good Algorithms

1. **Correctness**: The algorithm produces the correct output for all valid inputs
2. **Efficiency**: The algorithm uses reasonable time and memory resources
3. **Clarity**: The algorithm is easy to understand and implement
4. **Generality**: The algorithm works for a range of inputs, not just one specific case

## Example: Finding the Maximum Number

Let's start with a simple problem: finding the maximum number in a list.

### Approach 1: Naive Thinking
```python
# Just look at the list and pick the biggest number
numbers = [3, 7, 2, 9, 1]
# Answer: 9
```

This works for small lists, but it's not an algorithm - it's just observation. We need a systematic approach.

### Approach 2: Algorithmic Thinking
```python
def find_max(numbers):
    """
    Algorithm to find the maximum number in a list.
    
    Steps:
    1. Start with the first number as the current maximum
    2. Compare each remaining number with the current maximum
    3. If a number is larger, update the current maximum
    4. Return the maximum after checking all numbers
    """
    if not numbers:  # Handle empty list
        return None
    
    max_number = numbers[0]  # Step 1: Initialize with first number
    
    for number in numbers[1:]:  # Step 2: Check remaining numbers
        if number > max_number:  # Step 3: Compare and update
            max_number = number
    
    return max_number  # Step 4: Return result

# Test the algorithm
test_cases = [
    [3, 7, 2, 9, 1],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [42],
    [-5, -2, -10, -1]
]

for numbers in test_cases:
    result = find_max(numbers)
    print(f"Maximum of {numbers} is {result}")
```

**Output:**
```
Maximum of [3, 7, 2, 9, 1] is 9
Maximum of [1, 2, 3, 4, 5] is 5
Maximum of [5, 4, 3, 2, 1] is 5
Maximum of [42] is 42
Maximum of [-5, -2, -10, -1] is -1
```

## The Algorithmic Thinking Process

When solving problems algorithmically, follow these steps:

### 1. Understand the Problem
- What is the input?
- What is the expected output?
- Are there any constraints or edge cases?

### 2. Plan Your Approach
- Break the problem into smaller subproblems
- Think about what operations you need
- Consider different approaches

### 3. Write Pseudocode
- Describe your algorithm in plain language
- Don't worry about syntax yet
- Focus on the logic

### 4. Implement
- Translate pseudocode to code
- Use clear variable names
- Add comments for complex logic

### 5. Test
- Test with normal cases
- Test with edge cases (empty lists, single element, etc.)
- Test with boundary values

### 6. Analyze and Optimize
- Is your solution correct?
- Can it be made more efficient?
- Is it readable and maintainable?

## Example: Counting Occurrences

**Problem**: Count how many times a specific number appears in a list.

Let's apply our algorithmic thinking process:

### Step 1: Understand the Problem
- **Input**: A list of numbers and a target number
- **Output**: The count of how many times the target appears
- **Edge cases**: Empty list, target not in list, multiple occurrences

### Step 2: Plan Your Approach
- Initialize a counter to 0
- Go through each number in the list
- If the number matches the target, increment the counter
- Return the counter

### Step 3: Pseudocode
```
FUNCTION count_occurrences(numbers, target):
    SET counter = 0
    FOR EACH number IN numbers:
        IF number EQUALS target:
            INCREMENT counter
    RETURN counter
```

### Step 4: Implement
```python
def count_occurrences(numbers, target):
    """
    Count how many times target appears in numbers.
    
    Args:
        numbers: List of numbers
        target: Number to count
    
    Returns:
        Integer count of occurrences
    """
    counter = 0
    
    for number in numbers:
        if number == target:
            counter += 1
    
    return counter

# Test the algorithm
test_list = [1, 2, 3, 2, 4, 2, 5]
target = 2
result = count_occurrences(test_list, target)
print(f"The number {target} appears {result} times in {test_list}")
```

**Output:**
```
The number 2 appears 3 times in [1, 2, 3, 2, 4, 2, 5]
```

## Common Algorithmic Patterns

As you progress, you'll recognize common patterns:

1. **Iteration**: Going through data systematically
2. **Comparison**: Comparing elements to find relationships
3. **Accumulation**: Building up a result (sum, count, etc.)
4. **Transformation**: Converting data from one form to another
5. **Selection**: Choosing elements based on criteria

## Practice Exercises

### Exercise 1: Find Minimum
Write an algorithm to find the minimum number in a list. Test it with various inputs.

### Exercise 2: Sum of Even Numbers
Write an algorithm that sums all even numbers in a list.

### Exercise 3: Reverse a List
Write an algorithm that reverses a list without using built-in reverse methods.

### Exercise 4: Check if Sorted
Write an algorithm that checks if a list is sorted in ascending order.

## Practice Time!

**Great work!** You've reached the practice exercises.

Try to solve the problems above on your own before checking solutions.
When you're ready, you can:
- Check the solutions in the original markdown file
- Ask your instructor for help
- Discuss with classmates

Remember: The process of solving is more important than getting the answer immediately!

## Key Takeaways

1. **Algorithms are systematic procedures** - They follow clear, repeatable steps
2. **Good algorithms are correct, efficient, and clear** - Balance all three
3. **Follow a structured process** - Understand, plan, implement, test, optimize
4. **Practice is essential** - The more problems you solve, the better you'll recognize patterns

## Next Steps

In the next tutorial, we'll dive deeper into problem-solving strategies and learn how to break down complex problems systematically.
