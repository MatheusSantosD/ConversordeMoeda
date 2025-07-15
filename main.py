import customtkinter # Importa a biblioteca CustomTkinter para criar interfaces gráficas personalizadas.
from pegar_moedas import nomes_moedas, conversoes_disponiveis # Importa funções para obter nomes e conversões de moedas.
from pegar_cotacao import pegar_cotacao_moeda # Importa a função para pegar a cotação de uma moeda.

# --- Configuração Inicial da Janela ---
# Define o tema de aparência da aplicação como "dark" (escuro).
customtkinter.set_appearance_mode("dark")
# Define o esquema de cores padrão dos elementos da interface como "dark-blue".
customtkinter.set_default_color_theme("dark-blue")

# Cria a janela principal da aplicação.
janela = customtkinter.CTk()
# Define o tamanho da janela para 500x500 pixels.
janela.geometry("500x500")

# Obtém um dicionário de conversões disponíveis, onde a chave é a moeda de origem e o valor é uma lista de moedas de destino.
dic_conversoes_disponiveis = conversoes_disponiveis()

# Exemplo: dic_conversoes_disponiveis["USD"] => ["BRL", "CAD", "BTC", "AUD"]
# Isso significa que, se a moeda de origem for USD, as moedas de destino disponíveis serão BRL, CAD, BTC e AUD.

# --- Criação dos Elementos da Interface ---

# Cria um rótulo para o título da aplicação.
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("",20))
# Cria um rótulo para instruir o usuário a selecionar a moeda de origem.
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem")
# Cria um rótulo para instruir o usuário a selecionar a moeda de destino.
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino")

# --- Funções do Aplicativo ---

def carregar_moedas_destino(moeda_selecionada):
    """
    Atualiza as opções do campo de moeda de destino com base na moeda de origem selecionada.
    """
    # Obtém a lista de moedas de destino disponíveis para a moeda de origem selecionada.
    lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
    # Configura as novas opções no campo de seleção da moeda de destino.
    campo_moeda_destino.configure(values=lista_moedas_destino)
    # Define a primeira moeda da lista como a opção padrão no campo de moeda de destino.
    campo_moeda_destino.set(lista_moedas_destino[0])

# Cria um menu de opções (dropdown) para a moeda de origem.
# 'values' são as chaves (códigos das moedas) do dicionário de conversões disponíveis.
# 'command' define a função a ser chamada quando uma opção é selecionada (carregar_moedas_destino).
campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()),
                                                     command=carregar_moedas_destino)
# Cria um menu de opções (dropdown) para a moeda de destino.
# Inicialmente, exibe "Selecione uma moeda de origem" até que uma moeda de origem seja escolhida.
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["Selecione uma moeda de origem"])

def converter_moeda():
    """
    Pega as moedas selecionadas, obtém a cotação e exibe o resultado.
    """
    # Obtém a moeda de origem selecionada pelo usuário.
    moeda_origem = campo_moeda_origem.get()
    # Obtém a moeda de destino selecionada pelo usuário.
    moeda_destino = campo_moeda_destino.get()
    # Verifica se ambas as moedas foram selecionadas.
    if moeda_origem and moeda_destino:
        # Pega a cotação da moeda de origem para a moeda de destino.
        cotacao = pegar_cotacao_moeda(moeda_origem, moeda_destino)
        # Atualiza o rótulo com a cotação formatada.
        texto_cotacao_moeda.configure(text=f"1 {moeda_origem} = {cotacao} {moeda_destino}")

# Cria um botão "Converter" que, quando clicado, chama a função 'converter_moeda'.
botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda)

# Cria um frame rolável para exibir a lista de moedas disponíveis.
lista_moedas = customtkinter.CTkScrollableFrame(janela)

# Cria um rótulo vazio que será usado para exibir a cotação da moeda.
texto_cotacao_moeda = customtkinter.CTkLabel(janela, text="")

# Obtém um dicionário com todos os nomes das moedas disponíveis.
moedas_disponiveis = nomes_moedas()
# Itera sobre cada código de moeda no dicionário 'moedas_disponiveis'.
for codigo_moeda in moedas_disponiveis:
    # Obtém o nome completo da moeda usando o código.
    nome_moeda = moedas_disponiveis[codigo_moeda]
    # Cria um rótulo para cada moeda no frame rolável, exibindo o código e o nome.
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=f"{codigo_moeda}: {nome_moeda}")
    # Empacota (posiciona) o rótulo da moeda no frame rolável.
    texto_moeda.pack()

# --- Posicionamento dos Elementos na Tela ---
# O método .pack() é usado para organizar e posicionar os widgets na janela.
# 'padx' e 'pady' adicionam preenchimento horizontal e vertical, respectivamente.

# Posiciona o título.
titulo.pack(padx=10, pady=10)
# Posiciona o rótulo de seleção da moeda de origem.
texto_moeda_origem.pack(padx=10, pady=10)
# Posiciona o menu de opções da moeda de origem.
campo_moeda_origem.pack(padx=10)
# Posiciona o rótulo de seleção da moeda de destino.
texto_moeda_destino.pack(padx=10, pady=10)
# Posiciona o menu de opções da moeda de destino.
campo_moeda_destino.pack(padx=10)
# Posiciona o botão de conversão.
botao_converter.pack(padx=10, pady=10)
# Posiciona o rótulo onde a cotação será exibida.
texto_cotacao_moeda.pack(padx=10, pady=10)
# Posiciona o frame rolável com a lista de moedas.
lista_moedas.pack(padx=10, pady=10)

# --- Rodar a Janela ---
# Inicia o loop principal da aplicação, que mantém a janela aberta e responsiva a eventos.
janela.mainloop()
