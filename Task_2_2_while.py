'''
Перепишите предыдущий пример в виде функции find_person(name), которая ищет имя в списке.
'''

names=["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

def find_person(names_1):
 
    count=0
    while True:
        name=names_1[count]
        print('count  ', count,'name ', name)
        if name=='Валера':
            print('Валера нашелся')
            break
        else:
            count+=1

find_person(names)