import requests

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
print(requisicao)
print(requisicao.json())


dicionario = requisicao.json()

print(dicionario['USDBRL'])
print(dicionario['USDBRL']['high'])

