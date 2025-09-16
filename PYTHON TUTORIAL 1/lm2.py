if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    m=[]
    l=[[i,j,k] for i in range(x) for j in range(y) for k in range(z)]
    
    for a in range(len(l)):
        if l[a][0]+l[a][1]+l[a][2]!=n:
            m.append(l[a])
    print(m)