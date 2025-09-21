def longest_dividing_subsequence(arr):
    n = len(arr)
    best = [1] * n   # Best(i) initialized to 1

    for i in range(n):
        for j in range(i):
            if arr[i] % arr[j] == 0:  # divisibility condition
                best[i] = max(best[i], best[j] + 1)

    return max(best)


# Input handling
N = int(input().strip())
arr = [int(input().strip()) for _ in range(N)]

print(longest_dividing_subsequence(arr))
