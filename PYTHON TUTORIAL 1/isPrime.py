def isprime(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c=c+1
    return(c==0)
n=int(input("enter n"))
print(isprime(n))