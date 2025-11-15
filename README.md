# Maximum Value But Limited Neighbors

## Problem
Given an array `a[1..n]` of positive numbers and integer `k`:
- Create binary array `b[1..n]` (only 0s and 1s)
- Array `b` has at most `k` adjacent 1s
- Maximize sum: `∑(a[j] * b[j])`

**Adjacent 1s:** Count of consecutive 1-pairs in array
- `[0, 1, 1, 0]` has 1 adjacent pair
- `[1, 1, 1, 0]` has 2 adjacent pairs

## Examples

**Example 1:**
```
Array: [100, 300, 400, 50], k = 1
Result: b = [0, 1, 1, 0], sum = 700
```

**Example 2:**
```
Array: [10, 100, 300, 400, 50, 4500, 200, 30, 90], k = 2
Result: b = [1, 0, 1, 1, 0, 1, 1, 0, 1], sum = 5500
```

## Algorithm

**Dynamic Programming:** O(n × k) time and space

**State:** `dp[i][j][last]`
- `i` = position in array
- `j` = adjacent 1s used
- `last` = previous element selected (0/1)

**Logic:**
- If previous = 0: selecting current doesn't create adjacency
- If previous = 1: selecting current creates adjacency (j++)

## Usage
```bash
python3 project3.py
```

**Output:**
- Test cases with optimal binary array `b`
- Execution times for different array sizes