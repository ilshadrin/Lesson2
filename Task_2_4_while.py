

'''

4 При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”


'''



def get_answer():
    while True:
        user_say=input('Скажи мне что-нибудь ')
        if user_say=='Пока':
            print('Ну пока')
            break
        else:
            print('Ну нет, я не это хотел увидеть')







def ask_user():

    while True:
        get_answer()
        break
    ask_user()

