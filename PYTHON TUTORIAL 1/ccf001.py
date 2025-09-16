n=int(input())
l=[]
r=[0 for i in range(n)]
for i in range(n):
    s=input()
    l.append(s)
le=len(l)
for i in range(n):
    r[i]=0
    for j in range(2,len(l[i])):
        k=int(l[i][j])+int(l[i][j-1])+int(l[i][j-2])
        if k%3==0:
            r[i]=r[i]+1
for i in range(le):
    print(r[i])