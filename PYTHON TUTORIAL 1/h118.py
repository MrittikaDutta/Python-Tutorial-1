if __name__ == '__main__':
    n = int(input())
    l=[0,0,0,0]
    m=[]
    for i in range(n):
        k=input()
        m.append(k)
    for i in range(n):
        if m[i][0]=='i':
            b=len(m[i])
            l[m[b-1]]=l[b-3]
    print(l)