'''

Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
Посчитать и вывести средний балл по всей школе.
Посчитать и вывести средний балл по каждому классу.

'''


class_1a={'school_class': '1a', 'оценки': [3,3,4,5,2]}
class_1b={'school_class': '1b', 'оценки': [5,3,1,5,4]}
class_1c={'school_class': '1c', 'оценки': [3,4,3,5,2]}


lists_school=[class_1a,class_1b,class_1c]


def average_class(class_n,):
    
    count=0
    sum1=0
    for a in class_n['оценки']:
        a=class_n['оценки'][count]
        count=count+1
        sum1=sum1+a
        
    total1=sum1/(len(class_n['оценки']))
    print('Class № ',class_n['school_class'], 'Average count ', total1)
    return total1


ac1=average_class(class_1a)
ac2=average_class(class_1b)
ac3=average_class(class_1c)

print('Average for school  ',(ac1+ac2+ac3)/3)

'''

def sre(lists_school_n):
    count2=0
    for count2 in lists_school_n:
        
        def average_class(lists_school_n[count2]):
    
            count=0
            sum1=0
            for a in class_n['оценки']:
                a=class_n['оценки'][count]      
                count=count+1
                sum1=sum1+a
        
            total1=sum1/(len(class_n['оценки']))
            print('Class № ',class_n['school_class'], 'Average count ', total1)
            return total1

        print(lists_school_n[count2])
        count2=count2+1
'''