a,b=map(int,input().split())
c,d=map(int,input().split())
if (abs((c-a))==abs((d-b))) or (a==c or b==d):
    print('YES')
else:
    print('NO')