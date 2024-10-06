a,b=map(int,input().split())
c,d=map(int,input().split())
if abs((c-a))==abs((d-b)):
    print('YES')
else:
    print('NO')