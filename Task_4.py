'''
Установите модуль ephem
Добавьте в бота команду /planet, которая будет принимать на вход название планеты на английском.
При помощи условного оператора if и ephem.constellation научите бота отвечать, в каком созвездии сегодня находится планета.

'''


import ephem
planeta=input('Введите планету  ')

print(ephem.planeta('2016/10/23'))
#mars = ephem.planeta()
#print(ephem.constellation(mars))

