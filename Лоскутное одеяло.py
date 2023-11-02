import numpy    
lstr = ['1','2','3','4']   #Список строк,в будущем понадобится для проверки вводимых значений
lstolb = ['1','2','3','4','5']    #Список стролбцов,в будущем понадобится для проверки вводимых значений
pole = numpy.full((5,6),'-')
s=''
k1 = 0    #кол-во штрафных очков 1 игрока
k2 = 0    #кол-во штрафных очков 2 игрока
for i in range(5):     #создание нумерации строк и столбцов на поле
    pole[i][0] = i 
    pole[0][i] = i
pole[0][5] = 5
print(pole)
while True:
    print('1-ый игрок,введите куда хотите поставить свой символ($)\nВведите сначала строку,затем столбец')    
    while True:
        a = input()       
        b = input()
        if (a in lstr) and (b in lstolb): 
            a = int(a)
            b = int(b)         
            if (pole[a][b] != '$') and (pole[a][b] != '#'):
                pole[a][b] = '$'     
                break
            else:          
                print('Введите другое значение')
        else:           
            print('Введите другое значение')
    print(pole)  
    if pole[a][b] == pole[a-1][b]:
        k1 = k1+1   
    if (a != 4) and (pole[a][b] == pole[a+1][b]):
        k1 = k1+1  
    if pole[a][b] == pole[a-1][b-1]:
        k1 = k1+1  
    if (b != 5) and (pole[a][b] == pole[a-1][b+1]):
        k1 = k1+1 
    if pole[a][b] == pole[a][b-1]:
        k1 = k1+1 
    if (b != 5) and (b != 5) and (pole[a][b] == pole[a][b+1]):
        k1 = k1+1 
    if (a != 4) and (pole[a][b] == pole[a+1][b-1]):
        k1 = k1+1
    if (a != 4) and (b != 5) and (pole[a][b] == pole[a+1][b+1]):
        k1 = k1+1      
    print('2-ой игрок,введите куда хотите поставить свой символ(#)\nВведите сначала строка,затем столбец')
    while True:
        a = input()      
        b = input()
        if (a in lstr) and (b in lstolb):    
            a = int(a)
            b = int(b)
            if (pole[a][b] != '$') and (pole[a][b] != '#'):
                pole[a][b] = '#'
                break
            else:              
                print('Введите другое значение')
        else:
            print('Введите другое значение')
    print(pole)
    if pole[a][b] == pole[a-1][b]:
        k2 = k2+1  
    if (a != 4) and (pole[a][b] == pole[a+1][b]):
        k2 = k2+1   
    if pole[a][b] == pole[a-1][b-1]:
        k2 = k2+1   
    if (b != 5) and (pole[a][b] == pole[a-1][b+1]):
        k2 = k2+1    
    if pole[a][b] == pole[a][b-1]:
        k2 = k2+1
    if (b != 5) and (b != 5) and (pole[a][b] == pole[a][b+1]):
        k2 = k2+1
    if (a != 4) and (pole[a][b] == pole[a+1][b-1]):
        k2 = k2+1 
    if (a != 4) and (b != 5) and (pole[a][b] == pole[a+1][b+1]):
        k2 = k2+1
    if any('-' in i for i in pole):   #проверка на конец игры
        continue
    else:
        print(k1,' ',k2)
        if k1 > k2:
            print('Выиграл второй игрок!!!')
            break
        elif k1 < k2:
            print('Выиграл первый игрок!!!')
            break
        else:
            print('Ничья !!!')
            break
