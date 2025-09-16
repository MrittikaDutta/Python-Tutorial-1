def longest_fully_dividing_subsequence(N, sequence):
    Best = [1] * N
    for i in range(1, N):
        for j in range(i):
            if sequence[i] % sequence[j] == 0:
                Best[i] = max(Best[i], Best[j] + 1)
    return max(Best)

N = int(input())
sequence = []
for _ in range(N):
    sequence.append(int(input()))
result = longest_fully_dividing_subsequence(N, sequence)
print(result)
