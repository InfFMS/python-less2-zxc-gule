n=int(input())
a=0
for i in range(2,n+1):
    a=0
    for l in range(2,i):
        if i%l!=0:
            a+=0
        else:
            a+=1
    if a==0:
        print(i,end=' ')