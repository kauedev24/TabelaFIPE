"""Importação do selenium para automatização"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

navegador = webdriver.Edge()

navegador.get('https://veiculos.fipe.org.br/')
navegador.maximize_window()

# Ordem dos cliques -> copiar Xpath

# Primeiro clicar em consulta e utílitários pequenos
elemento = WebDriverWait(navegador, 10).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="front"]/div[1]/div[2]/ul/li[1]/a/div[2]')
)).click()


sleep(2)
# segundo clicar e selecionar o mes de pesquisa
navegador.find_element(
    By.XPATH, '//*[@id="selectTabelaReferenciacarro_chosen"]/a/div/b').click()

opcoes_mes_ano = navegador.find_elements(
    By.XPATH, '//*[@id="selectTabelaReferenciacarro_chosen"]/div/ul')
lista_mes_ano = opcoes_mes_ano[0].find_elements(By.CSS_SELECTOR, 'li')
lista_mes_ano[1].click()


sleep(2)
# terceiro clicar e selecionar a marca
navegador.find_element(
    By.XPATH, '//*[@id="selectMarcacarro_chosen"]/a/div/b').click()
opcoes_marca = navegador.find_elements(
    By.XPATH, '//*[@id="selectMarcacarro_chosen"]/div/ul')
lista_marca = opcoes_marca[0].find_elements(By.CSS_SELECTOR, 'li')
lista_marca[2].click()


sleep(2)
# quarto clicar e selecionar o modelo
navegador.find_element(
    By.XPATH, '//*[@id="selectAnoModelocarro_chosen"]/a/div/b').click()
opcoes_modelo = navegador.find_elements(
    By.XPATH, '//*[@id="selectAnoModelocarro_chosen"]/div/ul')
lista_modelo = opcoes_modelo[0].find_elements(By.CSS_SELECTOR, 'li')
lista_modelo[2].click()


sleep(2)
# quito clicar e selecionar ano/modelo
navegador.find_element(
    By.XPATH, '//*[@id="selectAnocarro_chosen"]/a/div/b').click()
opcoes_ano_modelo = navegador.find_elements(
    By.XPATH, '//*[@id="selectAnocarro_chosen"]/div/ul')
lista_ano_modelo = opcoes_ano_modelo[0].find_elements(By.CSS_SELECTOR, 'li')
lista_ano_modelo[3].click()


# sexto clicar e selecionar em pesquisar
navegador.find_element(By.LINK_TEXT, 'Pesquisar').click()


# ultimo salvar os dados da tabela em dicionários
sleep(10)
