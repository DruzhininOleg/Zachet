from random import choice
s='0123456789'
zadumch=choice(s[0:10])
for i in range(3):
    s=''.join(s.split(zadumch[i]))
    zadumch+=choice(s)
b=0 #кол-во быков
while b!=4:
    print('Введите предполагаемое число')
    chislo=input()
    k=0 #кол-во коров
    b=0
    t=0 #добавочная переменная проверяющая число на повторяющиеся цифры
    l=str(chislo) #перевод числа в строку
    stroka=str(zadumch) #перевод задуманного числа в строку
    if len(l)!=4:
        print('Число не подходит по кол-ву цифр')
        continue
    for i in range(4):
        if l[i]==zadumch[i]:
            b=b+1
        elif (l[i] in stroka) and (l[i]!=zadumch[i]):
            k=k+1
        if l.count(l[i])>1:
            t=1
            print('В числе есть повторяющиеся цифры,введите новое число')
            break
    if t==0:
        print('Быков=',b,'Коров=',k)
    if b==4:
        print('Вы выиграли')
