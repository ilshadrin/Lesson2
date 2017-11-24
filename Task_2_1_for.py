'''
Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
Посчитать и вывести средний балл по всей школе.
Посчитать и вывести средний балл по каждому классу.

'''

class_1a={'school_class': '1a', 'оценки': [3,3,4,5,2]}
class_1b={'school_class': '1b', 'оценки': [5,3,1,5,4]}
class_1c={'school_class': '1c', 'оценки': [3,4,3,5,2]}

lists_school=[class_1a,class_1b,class_1c]



av_school=0
for a1 in lists_school:
    sum1=0
    
    for a in a1['оценки']:
        sum1=sum1+a
    
    av_class=sum1/(len(a1['оценки']))
    av_school=av_school+av_class

    print('av_class  ',a1['school_class'], 'Average count ', av_class)
   
av_school_sum=av_school/len(lists_school)
print('Average for school ', av_school_sum)


'''
************
Старый, неверный код

**************

count1=0
av_school=0
for a1 in lists_school:
    a1=lists_school[count1]['оценки']
    count2=0
    sum1=0
    for a in a1:
        #print('a', a)
        a=a1[count2]
        sum1=sum1+a
        count2=count2+1
        #print('sum ', sum1)

    av_class=sum1/(5)
    av_school=av_school+av_class

    print('av_class  ',lists_school[count1]['school_class'], 'Average count ', av_class)
    #print('av_school ', av_school)
    #print('a1', a1)
    #print('count1', count1)
    count1=count1+1

av_school_sum=av_school/3
print('Average for school ', av_school_sum)
'''
