def limpf(n):
    e= map(int, input().split())
    v= map(int, input().split())
    r=[0 for i in range(n)]
    m=[]
    maximum=0
    for i in range(n):
        l=[]
        for j in range(i):
            r=e[i]*v[j]
            l.append(e[i]*v[j])
        m.append(max(r))
    for i in m:
        maximum+=i
    return(maximum)
    
if __name__ == '__main__':
    t=int(input())
    n=int(input())
    for i in range(t):
        print(limpf(n))