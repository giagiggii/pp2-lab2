x=int(input())
x1=int(input())
y=int(input())
y1=int(input())
if (x+x1)%2==0 and (y+y1)%2==0 :
    print('YES')
elif (x+x1)%2==0 and (y+y1)%2==1:    
        print('NO')
elif (x+x1)%2==1 and (y+y1)%2==1 : 
    print('YES')
elif (x+x1)%2==1 and (y+y1)%2==0:
    print('NO')