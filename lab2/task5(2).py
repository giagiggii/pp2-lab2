a=int(input())
b=int(input())
c=int(input())
if a<b and a<c:
    print(a)
elif b<a and b<c:
    print(b)
elif c<a and c<b:
    print(c)
elif a==b and a<c or b<c:
    print(a)