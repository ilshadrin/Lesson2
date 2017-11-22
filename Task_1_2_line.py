'''

Написать функцию, которая принимает на вход две строки.
Если строки одинаковые, возвращает 1.
Если строки разные и первая длиннее, возвращает 2.
Если строки разные и вторая строка 'learn', возвращает 3.


'''




def comparison(line1,line2):
    if  line1 == line2:
        print(1)

    elif len(line1)> len(line2):
         print(2)

    elif line2=='learn':
         print(3)    



line1=input('Please write line №1  ')
line2=input('Please write line №2  ')

comparison(line1,line2)