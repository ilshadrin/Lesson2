'''
Попросить пользователя ввести возраст.
По возрасту определить, чем он должен заниматься: учиться в детском саду, школе, ВУЗе или работать.
Вывести занятие на экран.

'''

age=int(input('Please write your age  '))

if age<7:
    print('Go to kindergarten')
elif 7<=age<18:
    print('Go to school')
elif 18<=age<23:
    print('Go to University')
elif 23<=age:
    print('Go to work')

