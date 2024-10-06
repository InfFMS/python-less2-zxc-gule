a=int(input())
if a<1 and a>12:
    print('Неверный номер месяца')
elif a<3 or a==12:
    print('Зима')
elif a>2 and a<=5:
    print('Весна')
elif a>5 and a<9:
    print('Лето')
elif a>=9 and a<12:
    print('Осень')