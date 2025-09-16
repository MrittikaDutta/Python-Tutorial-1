def factors(n):
    factorlist=[]
    for i in range(1,n+1):
        if n%i==0:
            factorlist=factorlist+[i]
    return(factorlist)
