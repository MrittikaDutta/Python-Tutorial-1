if __name__ == '__main__':
    m1=100
    m2=100
    l=[]
    m=[]
    k=[]
    n=int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        l.append(score)
        m.append(name)
    for i in range(n):
        if l[i]<=m1:
            m2=m1
            m1=l[i]
    for i in range(n):
        if l[i]==m2:
            k.append(m[i])
    k.sort()
    for i in k:
        print(i)                
        