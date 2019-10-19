from faker import Factory
from random import randint

class User:
    def name_generator(self):
        user = Factory.create('pt-BR')
        return user.name()
    
    def phone_generator(self):
        phone_list = ['(12) 98979-1914', '(68) 98849-5399','(84) 98296-8041', '(66) 98390-7390',
        '(83) 98851-1418', '(98) 98710-6944', '(92) 98193-9680', '(65) 98498-5600', '(62) 98113-5778',
        '(67) 99508-0328', '(63) 98337-7200', '(21) 98365-9665', '(51) 98447-9971', '(91) 99946-4927', '(95) 98988-2480']
        choice = randint(0, len(phone_list)-1)
        return phone_list[choice]

    def localization_generator(self):
        localization_list = [
            '-76.4566, 102.7829',
            '55.5506, 157.4857',
            '-2.3413, -112.2855',
            '-62.6360, -78.2815',
            '11.5834, 27.9677',
            '59.0167, -156.5852',
            '-84.9386, -83.9116',
            '24.4653, -77.8395',
            '4.2573, -119.1081',
            '-42.8133, -11.6806',
            '-24.2447, -99.9783',
            '6.0605, -3.7246']
        choice = randint(0, len(localization_list)-1)
        return  localization_list[choice]

    def city_generator(self):
        user = Factory.create(('pt-BR'))
        return user.city()

class Sensor:
    def localization_generator(self):
        localization_list = ['-23.113614 -46.927902', '-23.247917 -46.946097', '-23.215344 -46.954935',
        '-23.234493 -46.922434', '-23.234493 -46.922434', '-23.234493 -46.922434', '-23.234493 -46.922434',
        '-10.211980 -52.944779', '-10.169630 -52.916546']
        choice = randint(0, len(localization_list)-1)
        return localization_list[choice]

    def data_hora_generator(self):
        day = randint(1, 31)
        month = randint(1, 12)
        year = randint(2017, 2019)
        hour = randint(0, 23)
        minute = randint(0, 59)
        date = str(f'{day}/{month}/{year} - {hour}:{minute}')
    
    def celsius_generator(self):
        return randint(13, 35)

    