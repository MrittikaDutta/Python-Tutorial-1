def delchar(s,c):
    k=""
    for i in s:
        if i!=c:
            k=k+i
    return(k)
print(delchar("mrittika",'a'))
