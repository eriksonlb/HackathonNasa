import json
from app_generator import gerar_usuario, gerar_sensor
import requests


def gerar_json(dicionario):
    nome_arquivo = ('usuario.json' if dicionario == 'usuario' else 'sensor.json')
    with open(f'{nome_arquivo}', 'w') as f:
        json.dump(str(dicionario), f)

def json_sender(dicionario):
    headers = {'Content-type': 'application/json'}
    url = "https://sheet.best/api/sheets/12bd5c43-09c2-4412-83e8-398e1946672d"
    r = requests.post(url, data=json.dumps(dicionario), headers=headers)
    #time.sleep(1)

#Vai tentar gerar uma lista válida para um JSON, gerado na memória
try:
    print('Gerando sensor...\n')
    sensor_01 = gerar_sensor()
    print('Sensor gerado!\n')
except Exception as err: #se falhar, vai mostrar o erro +-
    print('Não foi possível gerar um sensor!', err)


#Vai tentar pegar os dados da lista, gerar um JSON e enviar para a tabela no link
try:
    print('\nEnviando o arquivo JSON...\n')
    json_sender(sensor_01)
    print(f'Arquivo JSON gerado:  \n{sensor_01}\n*Fim de arquivo*\n')
    print('JSON Enviado com sucesso!')
except Exception as err:
    print('Não foi possível enviar o JSON:', err)



#Comentei aqui para não ficar salvando o arquivo na pasta    
# try:
#     print('Criando arquivo JSON...\n')
#     gerar_json(sensor_01)
#     print('JSON gerado com sucesso!')
# except Exception as err:
#     print('Não foi possível gravar o JSON:', err)
