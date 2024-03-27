"""Importação do selenium para automatização"""
import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from pathlib import Path

# PATH_DATA = Path(__file__).parent / 'carro.json'

navegador = webdriver.Edge()

navegador.get('https://veiculos.fipe.org.br/')
navegador.maximize_window()

# Ordem dos cliques -> copiar Xpath

# 1º - clica em consulta e utílitários pequenos
elemento = WebDriverWait(navegador, 10).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="front"]/div[1]/div[2]/ul/li[1]/a/div[2]')
)).click()


sleep(2)
# 2º - clica e seleciona o mes de pesquisa
navegador.find_element(
    By.XPATH, '//*[@id="selectTabelaReferenciacarro_chosen"]/a/div/b').click()

opcoes_mes_ano = navegador.find_elements(
    By.XPATH, '//*[@id="selectTabelaReferenciacarro_chosen"]/div/ul')
lista_mes_ano = opcoes_mes_ano[0].find_elements(By.CSS_SELECTOR, 'li')
lista_mes_ano[1].click()


sleep(2)
# 3º - clica e seleciona a marca
navegador.find_element(
    By.XPATH, '//*[@id="selectMarcacarro_chosen"]/a/div/b').click()
opcoes_marca = navegador.find_elements(
    By.XPATH, '//*[@id="selectMarcacarro_chosen"]/div/ul')
lista_marca = opcoes_marca[0].find_elements(By.CSS_SELECTOR, 'li')
lista_marca[1].click()


sleep(2)
# 4º - clica e seleciona o modelo
navegador.find_element(
    By.XPATH, '//*[@id="selectAnoModelocarro_chosen"]/a/div/b').click()
opcoes_modelo = navegador.find_elements(
    By.XPATH, '//*[@id="selectAnoModelocarro_chosen"]/div/ul')
lista_modelo = opcoes_modelo[0].find_elements(By.CSS_SELECTOR, 'li')
lista_modelo[2].click()


sleep(2)
# 5º - clica e seleciona ano/modelo
navegador.find_element(
    By.XPATH, '//*[@id="selectAnocarro_chosen"]/a/div/b').click()
opcoes_ano_modelo = navegador.find_elements(
    By.XPATH, '//*[@id="selectAnocarro_chosen"]/div/ul')
lista_ano_modelo = opcoes_ano_modelo[0].find_elements(By.CSS_SELECTOR, 'li')
lista_ano_modelo[1].click()


sleep(2)
# 6º -  clica e seleciona botão pesquisar
navegador.find_element(By.LINK_TEXT, 'Pesquisar').click()

sleep(2)
# 7º - cria dicionário onde salvaremos os dados

# coleta os dados
tabela = navegador.find_elements(
    By.XPATH, '//*[@id="resultadoConsultacarroFiltros"]/table/tbody')
linhas = tabela[0].find_elements(By.CSS_SELECTOR, 'td')

# adiciona dados no dicionário
carro = {
    linhas[item].text: linhas[item + 1].text
    for item in range(0, len(linhas)-1, 2)
}


object_json = json.dumps(carro, indent=2, ensure_ascii=False)
with open('carro.json', 'w', encoding='utf-8') as file:
    file.write(object_json)
