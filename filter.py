l=[1,6,4,2,3,5,6,7,8,8]
def f(x):
    return x%2==0

m=list(filter(f,l))
print(l)
print(m)