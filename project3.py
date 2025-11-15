import time
import random

def max_value_limited_neighbors(a, k):
    """
    Find the maximum sum by selecting elements from array 'a' with at most 'k' adjacent 1s.
    
    Args:
        a: List of positive numbers
        k: Maximum number of adjacent 1s allowed
    
    Returns:
        Tuple of (maximum_sum, binary_array_b)
    
    Time Complexity of this algorithm will be O(n * k)
    """
    n = len(a)
    if n == 0:
        return 0, []
    
    # dp[i][j][last]: max sum at position i, with j adjacencies used, last element selected (0/1)
    INF = float('-inf')
    dp = [[[INF, INF] for _ in range(k + 2)] for _ in range(n + 1)]
    dp[0][0][0] = 0  # base case: position 0, 0 adjacencies, last not selected
    
    # Fill DP table
    for i in range(n):
        for j in range(k + 1):
            # Previous element NOT selected (last = 0)
            if dp[i][j][0] != INF:
                dp[i + 1][j][0] = max(dp[i + 1][j][0], dp[i][j][0])  # don't select current
                dp[i + 1][j][1] = max(dp[i + 1][j][1], dp[i][j][0] + a[i])  # select current
            
            # Previous element WAS selected (last = 1)
            if dp[i][j][1] != INF:
                dp[i + 1][j][0] = max(dp[i + 1][j][0], dp[i][j][1])  # don't select current
                if j < k:  # select current (creates adjacency)
                    dp[i + 1][j + 1][1] = max(dp[i + 1][j + 1][1], dp[i][j][1] + a[i])
    
    # Find maximum value at the end
    max_sum = INF
    best_j, best_last = -1, -1
    for j in range(k + 1):
        if dp[n][j][0] > max_sum:
            max_sum = dp[n][j][0]
            best_j, best_last = j, 0
        if dp[n][j][1] > max_sum:
            max_sum = dp[n][j][1]
            best_j, best_last = j, 1
    
    # Backtrack to construct array b
    b = [0] * n
    curr_j, curr_last = best_j, best_last
    
    for i in range(n, 0, -1):
        if curr_last == 1:  # current position is selected
            b[i - 1] = 1
            # Check where this state came from
            if curr_j > 0 and dp[i - 1][curr_j - 1][1] + a[i - 1] == dp[i][curr_j][1]:
                curr_j, curr_last = curr_j - 1, 1  # came from adjacent state
            elif dp[i - 1][curr_j][0] + a[i - 1] == dp[i][curr_j][1]:
                curr_last = 0  # came from non-adjacent state
        else:  # current position not selected
            b[i - 1] = 0
            # Check where this state came from
            if dp[i - 1][curr_j][0] == dp[i][curr_j][0]:
                curr_last = 0
            elif dp[i - 1][curr_j][1] == dp[i][curr_j][0]:
                curr_last = 1
    
    return max_sum, b


def count_adjacent_ones(b):
    """Count the number of adjacent 1s in binary array b."""
    count = 0
    for i in range(len(b) - 1):
        if b[i] == 1 and b[i + 1] == 1:
            count += 1
    return count


# Test with example cases from problem statement
print("Test Case 1:")
a1 = [100, 300, 400, 50]
k1 = 1
max_sum1, b1 = max_value_limited_neighbors(a1, k1)
print(f"Array a: {a1}")
print(f"k = {k1}")
print(f"Array b: {b1}")
print(f"Maximum sum: {max_sum1}")
print(f"Adjacent 1s: {count_adjacent_ones(b1)}")
print()

print("Test Case 2:")
a2 = [10, 100, 300, 400, 50, 4500, 200, 30, 90]
k2 = 2
max_sum2, b2 = max_value_limited_neighbors(a2, k2)
print(f"Array a: {a2}")
print(f"k = {k2}")
print(f"Array b: {b2}")
print(f"Maximum sum: {max_sum2}")
print(f"Adjacent 1s: {count_adjacent_ones(b2)}")
print()

# Measure execution time for different values of n
print("=" * 50)
print("Execution Time Analysis")
print("=" * 50)

sizes = [10, 50, 100, 200, 500, 1000, 2000]
k_value = 5

print(f"\nTesting with k = {k_value}\n")
print(f"{'n':>6} {'Time (seconds)':>20}")
print("-" * 30)

for n in sizes:
    random.seed(42)
    a = [random.randint(1, 1000) for _ in range(n)]
    
    start = time.perf_counter()
    _ = max_value_limited_neighbors(a, k_value)
    end = time.perf_counter()
    
    elapsed = end - start
    print(f"{n:6d} {elapsed:20.6f}")