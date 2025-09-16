n=int(input())
r=[0 for i in range(n)]
for i in range(n):
    s=input()
    for j in range(len(s)-2):
        k=ord(s[j])+ord(s[j+1])+ord(s[j+2])
        if k%3==0:
            r[i]+=1
for i in range(n):
    print(r[i])
