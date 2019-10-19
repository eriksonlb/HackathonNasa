from generator import User, Sensor
from random import randint

def gerar_usuario():
    fake_user = User()
    nome = fake_user.name_generator()
    fone = fake_user.phone_generator()
    cidade = fake_user.city_generator()
    local = fake_user.localization_generator()
    usuario = {
        'nome': nome,
        'fone': fone,
        'cidade': cidade,
        'geolocalizacao': local
    }

    return usuario

def gerar_sensor():
    fake_sensor = Sensor()
    local = fake_sensor.localization_generator()
    data = fake_sensor.data_hora_generator()
    sensor = {
        'id': id,
        'localizacao': local,
        'data': data,
        'notificado': True
    }

    return sensor
