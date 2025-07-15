# Importa a biblioteca 'requests' que permite fazer requisições HTTP pela internet
import requests

# Define uma função chamada 'pegar_cotacao_moeda' que recebe duas moedas como parâmetro:
# 'moeda_origem' (por exemplo, 'USD') e 'moeda_destino' (por exemplo, 'BRL')
def pegar_cotacao_moeda(moeda_origem, moeda_destino):
    # Monta o link da API para pegar a cotação, usando o f-string para inserir as moedas na URL
    link = f"https://economia.awesomeapi.com.br/last/{moeda_origem}-{moeda_destino}"

    # Envia uma requisição GET para o link e armazena a resposta na variável 'requisicao'
    requisicao = requests.get(link)

    # Converte a resposta em JSON e acessa o valor do 'bid' (preço de compra) da cotação
    # O dicionário retornado tem como chave o nome das moedas juntas (ex: 'USDBRL')
    cotacao = requisicao.json()[f"{moeda_origem}{moeda_destino}"]["bid"]

    # Retorna o valor da cotação
    return cotacao


# 200 - requisição funcionou
