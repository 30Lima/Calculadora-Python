#Realizando as importações necessárias.
import pprint
import requests

#Realizando uma pequena estilização no terminal.
print(4 * "\n")
print(50 * "=")
print(10 * " ", "CONECTANDO PYTHON COM API")
print(50 * "=")
print()

#Solicitando o CEP ao usuário.
cep = input("Por gentileza, digite o seu CEP:")

#Pegando o CEP digitado e buscando o mesmo na api 'viacep'.
url = f'https://viacep.com.br/ws/{cep}/json'

#Realizando a requisição na API com base no CEP digitado.
response = requests.get(url)

#Caso a conexão esteja certa, realizar o print com os dados do CEP.
if response.status_code == 200:
    data = response.json()
    print(data.keys())

    pprint.pprint(data)

#Caso ocorra um erro na solicitação, imprimir um aviso ao usuário e mostrar o código do erro.
else:
    print("Falha na solicitação. Código de status:", response.status_code)
