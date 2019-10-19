import json
from app_generator import gerar_usuario, gerar_sensor

def gerar_json(dicionario):
    nome_arquivo = ('usuario.json' if dicionario == 'usuario' else 'sensor.json')
    with open('meu_arquivo.json', 'w') as f:
        json.dump(dicionario, f)

gerar_json(str(gerar_usuario()))