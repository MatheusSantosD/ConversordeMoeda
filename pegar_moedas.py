# Importa a biblioteca xmltodict, que converte arquivos XML em dicionários Python
import xmltodict

# Função para ler os nomes das moedas a partir de um arquivo XML
def nomes_moedas():
    # Abre o arquivo 'moedas.xml' no modo de leitura binária ('rb') como 'arquivo_moedas'
    with open("moedas.xml", "rb") as arquivo_moedas:
        # Converte o conteúdo XML em dicionário usando xmltodict.parse
        dic_moedas = xmltodict.parse(arquivo_moedas)

    # Pega o conteúdo principal do XML acessando a chave 'xml'
    moedas = dic_moedas["xml"]

    # Retorna o dicionário com as moedas
    return moedas

# Função para organizar as conversões disponíveis a partir de um arquivo XML
def conversoes_disponiveis():
    # Abre o arquivo 'conversoes.xml' no modo de leitura binária ('rb') como 'arquivo_conversoes'
    with open("conversoes.xml", "rb") as arquivo_conversoes:
        # Converte o conteúdo XML em dicionário
        dic_conversoes = xmltodict.parse(arquivo_conversoes)

    # Pega o conteúdo principal do XML acessando a chave 'xml'
    conversoes = dic_conversoes["xml"]

    # Cria um dicionário vazio para armazenar as conversões disponíveis
    dic_conversoes_disponiveis = {}

    # Percorre cada par de conversão no dicionário 'conversoes'
    for par_conversao in conversoes:
        # Divide o par no caractere '-' separando a moeda de origem e destino
        moeda_origem, moeda_destino = par_conversao.split("-")

        # Se a moeda de origem já estiver no dicionário, adiciona a moeda de destino à lista existente
        if moeda_origem in dic_conversoes_disponiveis:
            dic_conversoes_disponiveis[moeda_origem].append(moeda_destino)
        else:
            # Se não existir ainda, cria uma nova lista com a moeda de destino
            dic_conversoes_disponiveis[moeda_origem] = [moeda_destino]

    # Retorna o dicionário organizado com as conversões disponíveis
    return dic_conversoes_disponiveis
