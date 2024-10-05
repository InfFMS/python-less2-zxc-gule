a=int(input())
b=int(input())
c=int(input())
d=int(input())
m=0
n=0
if a>=c and b<=d:
    m=a
    n=b
elif (c>=a and d<=b):
    m=c
    n=d
elif a>=c and d<=b:
    m=a
    n=d
elif a<=c and d>=b:
    m=c
    n=b
elif (a<=c and b<=c) or (a>=d and b>=d):
    print("пустое множество")
if m!=n:
    print('['+str(m)+','+str(n)+']')
else:
    print('['+str(m)+']')