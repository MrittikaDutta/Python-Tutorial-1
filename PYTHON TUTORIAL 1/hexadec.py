h="0123456789ABCDEF"
number=int(input())
for i in range(1,number+1):
    j=i
    s=""
    while j>0:
        if j%16==0:
            s="0"+s
            j=j//16
        else:
            s=h[j%16]+s
            j=j//16
    print(s)
        