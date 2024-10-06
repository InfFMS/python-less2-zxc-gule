a=int(input())
if a%10==1 and (((a%100-a%10))//10)!=1:
    print(str(a)+' год')
elif a%10<5 and (((a%100-a%10))//10)!=1:
    print(str(a)+' года')
elif (a//10-a%10)!=1:
    print(str(a)+' лет')
else:
    print(str(a)+' лет')