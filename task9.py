a,b=map(int,input().split())
c,d=map(int,input().split())
if (abs(a-c)==2 or abs(b-d)==2) and (abs(d-b)==1 or abs(a-c)==1):
    print("YES")
else:
    print("NO")