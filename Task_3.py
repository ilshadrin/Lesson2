
'''
Переписать функцию ask_user(), добавив обработку exception-ов
Добавить перехват ctrl+C и прощание

'''


def ask_user():
    
        while True:
            try:    
                user_say=input('Как дела?  ')
                if user_say=='Хорошо':
                        print('Ну пока, раз хорошо')
                        break
                else:
                    print('Ну нет, я не это хотел увидеть')

            except KeyboardInterrupt:
                return  print("Неееееет")

ask_user()
    
    