def f(x):
    x=x*x
l=[]
t={}
t["hey"]=56
x=[56,90,80]
for i in x:
    x=f(x)
for i in range(5):
    j=int(input())
    l.append(j)
map(f(l))
print([f(x) for i in range(10) if i%2==0])