def solve(s):
    
    b=s[0].upper()
    for i in range(0,len(s)-1):
        if s[i]==" ":
            
            k=s[i+1].upper()
            b=b+k
        else:
            b=b+s[i+1]
    return(b)

if __name__ == '__main__':
    g=input()
    solve(g)
    print(solve(g))