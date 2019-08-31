import os
while True:
    Celsius = input('Введите температуру по Цельсию: ')
    try:
        Celsius = float(Celsius)
        Fahrenheit = Celsius * 1.8 + 32
        Kelvin = Celsius + 273.15
        print('Температура по Фаренгейту:', round(Fahrenheit, 1))
        print('Температура в Кельвинах:', round(Kelvin, 1))
        os.system('pause')
        os.system('cls')
    except ValueError:
        os.system('cls')
