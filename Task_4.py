'''
Установите модуль ephem
Добавьте в бота команду /planet, которая будет принимать на вход название планеты на английском.
При помощи условного оператора if и ephem.constellation научите бота отвечать, в каком созвездии сегодня находится планета.

'''
import ephem



def space():

    planeta=input('Введите планету  ')
    date=input('Введите дату согласно формату ГГГГ/ММ/ДД ')

    if planeta =='Mars' :
        mars = ephem.Mars(date)
        print(ephem.constellation(mars))

    elif planeta =='Mercury' :
        mercury  = ephem.Mercury(date)
        print(ephem.constellation(mercury))

    elif planeta =='Venus' :
        venus = ephem.Venus(date)
        print(ephem.constellation(venus))

    elif planeta =='Jupiter' :
        jupiter = ephem.Jupiter(date)
        print(ephem.constellation(jupiter))

    elif planeta =='Saturn' :
        saturn  = ephem.Saturn (date)
        print(ephem.constellation(saturn))

    elif planeta =='Uranus' :
        uranus = ephem.Mars(date)
        print(ephem.constellation(uranus))

    elif planeta =='Neptune' :
        neptune = ephem.Neptune(date)
        print(ephem.constellation(neptune))

    elif planeta =='Pluto' :
        pluto  = ephem.Pluto(date)
        print(ephem.constellation(pluto ))


space()