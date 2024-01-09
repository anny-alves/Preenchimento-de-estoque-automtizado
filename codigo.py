# Bot de automação para preencher o sistema de estoque de uma tabela
# com dados de uma tabela
# por @AnnyAlves

# Importa a biblioteca para controle automático
import pyautogui

# Configura uma pausa de 0.3 segundos entre cada ação
pyautogui.PAUSE = 0.3 

# Abre o navegador (Chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Define o link para o sistema
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# Passo 2 - Fazer login
pyautogui.press("tab")
email = "annycalvess@gmail.com"
pyautogui.write(email)
pyautogui.press("tab")
senha = "1234"
pyautogui.write(senha)
pyautogui.press("tab")
pyautogui.press("enter")

# Importa a biblioteca pandas para manipulação de dados
import pandas as pd

# Lê o arquivo CSV de produtos
tabela = pd.read_csv("produtos.csv")

# Exibe a tabela para verificação
print(tabela)

# Passo 4 - Cadastrar produto
for linha in tabela.index:
    # Preenche o código do produto
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "codigo"]))

    # Preenche a marca do produto
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))

    # Preenche o tipo do produto
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))

    # Preenche a categoria do produto
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))

    # Preenche o preço unitário do produto
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))

    # Preenche o custo do produto
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))

    # Preenche a observação do produto se houver
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
        
    # Confirma o cadastro do produto
    pyautogui.press("tab")
    pyautogui.press("enter")

    # Atualiza a página (F5) para o próximo cadastro
    pyautogui.press("F5")

