from generator import User, Sensor #importar o arquivo generator.py
from random import randint, randrange 


def gerar_usuario(): #vou usar a classe Usuario pra criar um usuario fake com atributos abaixo
    fake_user = User() #instanciei a classe User
    nome = fake_user.name_generator()
    fone = fake_user.phone_generator()
    cidade = fake_user.city_generator()
    local = fake_user.localization_generator()
    #esses dados serão organizados num dicionário
    usuario = [{
        'nome': nome,
        'fone': fone,
        'cidade': cidade,
        'geolocalizacao': local
    }]
    return usuario #retorna um dicionario que será tratado no json_generator

def gerar_sensor(): #gerar sensor fake com atributos da classe Sensor
    fake_sensor = Sensor() #instanciei a classe Sensor
    local = fake_sensor.localization_generator()
    data = fake_sensor.data_hora_generator()   
    temperaturaFake = fake_sensor.randomTemperatura() #True ou False aleatório
    # temperaturaSensor = fake_sensor.temperaturaSensor() #Dados sensor

    #gerei um dicionario com os dados
    sensor = [ {
        'id': randrange(1, 121),
        'localizacao': local,
        'data': data,
        'temperatura': temperaturaFake,
        # 'temperatura': temperaturaSensor, #se for usar o sensor, descomentar
        'notificado': True
    }]
    return sensor #retorna um dicionario pra ser tratador em json_generator.py

