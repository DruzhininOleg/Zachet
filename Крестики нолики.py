import numpy
def fun(p):
    for i in p:
        if i == ' ':
            return False
    return True
pole = numpy.matrix([[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']])
f = True
while f == True: 
    print('Первый игрок введите куда хотите поставить крестик на поле')
    proverka = False
    while proverka == False:
        a = input()
        if a in ['0','1','2','3','4','5','6','7','8','9']:#проверка на то,является ли вводимый символ числом
            a = int(a)
        else:
            print('Введите число!')
            continue
        b = input()
        if b in ['0','1','2','3','4','5','6','7','8','9']:#проверка на то,является ли вводимый символ числом
            b = int(b)
        else:
            print('Введите число!')
            continue
        if ((a < 0) or (a >2)) or ((b < 0) or (b > 2)):
            print('Число не подходит под размер поля,введите другие числа')
            continue
        if (pole[a,b] == 'x') or (pole[a,b] == '0'):
            print('Эта ячейка уже занята,введите другую')
        else:
            pole[a,b] = 'x'
            print(pole)
            proverka = True
    if ((pole[0,0]==pole[0,1]==pole[0,2])and(pole[0,0]!=' ')) or ((pole[1,0]==pole[1,1]==pole[1,2])and(pole[1,0]!=' ')) or ((pole[2,0]==pole[2,1]==pole[2,2])and(pole[2,0]!=' ')) or ((pole[0,0]==pole[1,1]==pole[2,2])and(pole[0,0]!=' '))or  ((pole[2,0]==pole[1,1]==pole[0,2])and(pole[0,2]!=' ')) or ((pole[0,0]==pole[1,0]==pole[2,0])and(pole[1,0]!=' ')) or  ((pole[0,1]==pole[1,1]==pole[2,1])and(pole[0,1]!=' ')) or ((pole[0,2]==pole[1,2]==pole[2,2])and(pole[0,2]!=' ')):
        print('Первый игрок выиграл')
        f = False
        break
    if  fun(pole) == False:
        print('Второй игрок введите куда хотите поставить нолик на поле')
    else:
        print('Ничья!')
        f = False
    proverka = False
    while proverka == False:
        a = input()
        if a in ['0','1','2','3','4','5','6','7','8','9']:#проверка на то,является ли вводимый символ числом
            a=int(a)
        else:
            print('Введите число!')
            continue
        b = input()
        if b in ['0','1','2','3','4','5','6','7','8','9']:#проверка на то,является ли вводимый символ числом
            b = int(b)
        else:
            print('Введите число!')
            continue
        if ((a < 0)or(a > 2))or((b < 0)or(b > 2)):
            print('Число не подходит под размер поля,введите другие числа')
            continue 
        if (pole[a,b] == 'x') or (pole[a,b] == '0'):
            print('Эта ячейка уже занята,введите другую')
        else:
            pole[a,b] = '0'
            print(pole)
            proverka = True
    if ((pole[0,0]==pole[0,1]==pole[0,2])and(pole[0,0]!=' ')) or ((pole[1,0]==pole[1,1]==pole[1,2])and(pole[1,0]!=' ')) or ((pole[2,0]==pole[2,1]==pole[2,2])and(pole[2,0]!=' ')) or ((pole[0,0]==pole[1,1]==pole[2,2])and(pole[0,0]!=' '))or  ((pole[2,0]==pole[1,1]==pole[0,2])and(pole[0,2]!=' ')) or ((pole[0,0]==pole[1,0]==pole[2,0])and(pole[1,0]!=' ')) or  ((pole[0,1]==pole[1,1]==pole[2,1])and(pole[0,1]!=' ')) or ((pole[0,2]==pole[1,2]==pole[2,2])and(pole[0,2]!=' ')):
        print('Второй игрок выиграл')
        f = False
        break
        
    
