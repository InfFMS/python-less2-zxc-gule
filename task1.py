a=int(input())
b=(8+((55*(a-1)+20+10)//60))
n=((20+55*(a-1)+10)%60)
m=(8+((55*a+20)//60))
l=((20+55*a)%60)
if a<5 and a!=3:
    print('Время начала урока - '+str(b)+'.'+str(n)+', Время конца - '+str(m)+'.'+str(l))
elif a>=5:
    print('Время начала урока - '+str(12+((a-5)*45+30)//60)+'.'+str((20+(a-5)*55+10)%60)+', Время конца - '+str(12+((a-4)*45+30)//60)+'.'+str((20+(a-4)*55)%60))
if a==3:
    print('Время начала урока - 10.20, Время конца - 11.05')