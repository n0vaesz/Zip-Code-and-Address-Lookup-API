import requests

cep = "20090002"

link = f'https://viacep.com.br/ws/{cep}/json/'

requisicao = requests.get(link)

print(requisicao)

dic_requisicao = requisicao.json()

uf = dic_requisicao['uf']
cidade = dic_requisicao['localidade']
bairro = dic_requisicao['bairro']
print(uf, cidade, bairro)