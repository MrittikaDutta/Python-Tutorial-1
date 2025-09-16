def longest_fully_dividing_subsequence(N, sequence):
    # Initialize an array to store the lengths of the longest fully dividing sequences
    Best = [1] * N

    # Iterate through the input sequence
    for i in range(1, N):
        for j in range(i):
            if sequence[i] % sequence[j] == 0:
                # Update Best[i] if a longer fully dividing subsequence is found
                Best[i] = max(Best[i], Best[j] + 1)

    # Return the maximum value in the Best array, which represents the length of the longest fully dividing subsequence
    return max(Best)

# Read input
N = int(input())
sequence = []
for _ in range(N):
    sequence.append(int(input()))

# Calculate and print the length of the longest fully dividing subsequence
result = longest_fully_dividing_subsequence(N, sequence)
print(result)
