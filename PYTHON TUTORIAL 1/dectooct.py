oct="012345678"
number=int(input())
for i in range(1,number+1):
    j=i
    s=""
    while j>0:
        if j%8==0:
            s="0"+s
            j=j//8
        else:
            s=oct[j%8]+s
            j=j//8
    print(s)