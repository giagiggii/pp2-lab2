n=int(input())
m=int(input())
x=int(input())
y=int(input())
if m<n and m<x and m<y:
    print(m)
elif x<n and x<m and x<y:
    print(x)
elif y<n and y<m and y<x:
    print(y)