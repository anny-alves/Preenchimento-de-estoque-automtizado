# Bot de automação

# Passo a passo do projeto


# Passo 1- entrar no sistema da empresa -> https://dlp.hashtagtreinamentos.
# com/python/intensivao/login
import pyautogui
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
print("passou")

# from selenium import webdriver
# navegador = webdriver.Chrome()
# navegador.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")



# link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# pyautogui.press("enter")



# Passo 2 - Fazer login
# Passo 3 - Importar base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")
# print(tabela)
# Passo 4 - Cadastrar produto
# Passo 5 - Repetir até acabar a base de dados

