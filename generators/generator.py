from geopy.geocoders import Nominatim
from faker import Factory
from random import randint
import serial
import json
import random 
import time 

#Classe apenas pra gerar um usuario FAKE caso necessário
class User:
    def name_generator(self):
        #A lib Faker gera dados aleatórios,
        #com esse comando eu defino que quero dados aleatórios brasileiros
        user = Factory.create('pt-BR') 
        return user.name() #retorna nome aleatório
    
    def phone_generator(self): #lista de numeros que fui gerando do site 4Devs
        phone_list = ['(12) 98979-1914', '(68) 98849-5399','(84) 98296-8041', '(66) 98390-7390',
        '(83) 98851-1418', '(98) 98710-6944', '(92) 98193-9680', '(65) 98498-5600', '(62) 98113-5778',
        '(67) 99508-0328', '(63) 98337-7200', '(21) 98365-9665', '(51) 98447-9971', '(91) 99946-4927', '(95) 98988-2480']
        choice = randint(0, len(phone_list)-1) #pego um numero inteiro aleatório  de 0 até o tamanho da lista
        return phone_list[choice] #seto esse numero inteiro como index da lista de telefones

    def localization_generator(self):
        sensor = Factory.create(('pt-BR'))
        return sensor.city() #retorna uma cidade aleatória brasileira para o usuario

    def city_generator(self): #falta implementar
        None
#Classe apenas pra gerar um sensor FAKE caso necessário
class Sensor:
    def localization_generator(self): # pegar latitude e longitude de uma das cidades abaixo, que serão escolhidas aleatoriamente
        geolocator = Nominatim(user_agent="farofa-lactea")        
        city_list = ['Apuí', 'Altamira', 'Porto Velho', 'Caracaraí', 'São Félix do Xingu',
        'Novo Progresso', 'Lábrea', 'Colniza', ]
        index = randint(0, len(city_list)-1) #index aleatorio
        city = city_list[index] #pegar cidade pelo index
        city = geolocator.geocode(city) #pegar os dados da cidade escolhida
        latitude, longitude = city.latitude, city.longitude
        return str(f'{latitude}, {longitude}') #retorna os dados em umastring

    def data_hora_generator(self): #gerador de uma data
        day = randint(1, 31)
        month = randint(1, 12)
        year = randint(2017, 2019)
        hour = randint(00, 23)
        minute = randint(00, 59)
        date = str(f'{day}/{month}/{year} - {hour}:{minute}')
        return date
    
    def temperaturaSensor(self): #le o sensor pelo usb e seta em um dicionario
        with serial.Serial('COM5', 9600, timeout=2) as ser:
            while 1:
                tempBruto = ser.readline() # read one byte
                tempTratada = tempBruto.decode("utf-8")[:-2]
                return ("OK" if tempTratada == "OK" else "Fire!") #verificação do limite da temperatura de incendio


    def randomTemperatura(self): #gerador pra quando não tiver sensor plugado
        choice = randint(0, 1)
        return (True if choice == 1 else False) 



    