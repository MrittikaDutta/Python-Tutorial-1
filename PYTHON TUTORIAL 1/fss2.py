def subseq(n, l):
    Best = [1] * n

    for i in range(n):
        for j in range(i):
            if l[i] % l[j] == 0:
                Best[i] = max(Best[i], Best[j] + 1)

    return max(Best)

n = int(input())
l = []

for i in range(n):
    a = int(input())
    l.append(a)

print(subseq(n, l))