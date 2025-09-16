def merge_the_tools(string, k):
    l=len(string)
    f=l//k
    b=0
    r=0
    m=0
    z=""
    a=[""for i in range(f)]
    while m<l:
        a[b]=a[b]+string[m]
        r=r+1
        m=m+1
        if r>=3:
            r=0
            b=b+1
    for i in range(f):
        z=z+a[i]
    


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)