if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    k=-100
    m=-100
    for i in arr:
        if i>k:
            k=i
    for j in arr:
        if j>m and j<k:
            m=j
print(m)