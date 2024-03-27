"""Importação do selenium para automatização"""
import json
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Edge()

# cliques -> copiar Xpath


def seleciona_mes_ano():
    """seleciona mes e ano da pesquisa."""

    navegador.find_element(
        By.XPATH,
        '//*[@id="selectTabelaReferenciacarro_chosen"]/a/div/b').click()

    opcoes_mes_ano = navegador.find_elements(
        By.XPATH, '//*[@id="selectTabelaReferenciacarro_chosen"]/div/ul')

    return opcoes_mes_ano[0].find_elements(
        By.CSS_SELECTOR, 'li')


def seleciona_marca(indice):
    """seleciona a marca"""

    sleep(2)
    elemento_clique = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((
            By.XPATH,
            '//*[@id="selectMarcacarro_chosen"]/a/div/b'))).click()

    opcoes_marca = navegador.find_elements(
        By.XPATH, '//*[@id="selectMarcacarro_chosen"]/div/ul')

    lista_marca = opcoes_marca[0].find_elements(
        By.CSS_SELECTOR, 'li')

    lista_marca[indice].click()


def seleciona_modelo():
    """seleciona o modelo."""

    sleep(2)
    navegador.find_element(
        By.XPATH, '//*[@id="selectAnoModelocarro_chosen"]/a/div/b').click()

    opcoes_modelo = navegador.find_elements(
        By.XPATH, '//*[@id="selectAnoModelocarro_chosen"]/div/ul')

    return opcoes_modelo[0].find_elements(
        By.CSS_SELECTOR, 'li')


def seleciona_ano_modelo():
    """seleciona ano/modelo."""

    sleep(2)
    navegador.find_element(
        By.XPATH, '//*[@id="selectAnocarro_chosen"]/a/div/b').click()

    opcoes_ano_modelo = navegador.find_elements(
        By.XPATH, '//*[@id="selectAnocarro_chosen"]/div/ul')

    return opcoes_ano_modelo[0].find_elements(
        By.CSS_SELECTOR, 'li')


def move_telas(times):
    """move a tela para encontrar determinado clique."""

    sleep(2)
    for _ in range(0, times):
        navegador.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_UP)


navegador.get('https://veiculos.fipe.org.br/')
navegador.maximize_window()

sleep(2)
# 1º - clica em consulta e utílitários pequenos
elemento = WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((
        By.XPATH,
        '//*[@id="front"]/div[1]/div[2]/ul/li[1]/a/div[2]'))).click()

carros = {}
numero_carro = 0

start = datetime.now()
print(start)

sleep(2)
# 2º - clica e seleciona o mes/ano de pesquisa
lista_mes_ano = seleciona_mes_ano()
sleep(2)
for mes_ano in range(0, 1):
    lista_mes_ano[mes_ano].click()

    # 3º - clica e seleciona a marca
    seleciona_marca(0)  # FIAT código 28.Acura código 0

    # 4º - clica e seleciona o modelo
    lista_modelos = seleciona_modelo()

    print(f'Quantidade de modelos: {len(lista_modelos)}\n')

    for modelo in range(0, len(lista_modelos)):
        print("*"*10, "MODELO", modelo, "*"*10)

        lista_modelos[modelo].click()

        # 5º - clica e seleciona ano/modelo
        lista_ano_modelo = seleciona_ano_modelo()

        for ano_modelo in range(0, len(lista_ano_modelo)):
            lista_ano_modelo[ano_modelo].click()

            # 6º -  clica e seleciona botão pesquisar
            sleep(2)
            navegador.find_element(By.LINK_TEXT, 'Pesquisar').click()

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

            # agrupa os dados em um arquivo final .json
            carros[numero_carro] = carro
            print(f"Carro: {carros[numero_carro]}")
            print(15*'-')
            numero_carro += 1
            sleep(2)

            # sobe a tela 3 vezes para encontrar o clique ano_modelo
            move_telas(3)
            lista_ano_modelo = seleciona_ano_modelo()

        sleep(2)
        # MARCA
        move_telas(7)
        sleep(2)
        # reset no campo marca, esse indice precisa ser diferente da marca que estamos trocando os dados
        seleciona_marca(1)

        sleep(2)

        seleciona_marca(0)

        lista_modelos = seleciona_modelo()

    # TABELA MES ANO
    move_telas(7)
    seleciona_marca(1)

    lista_mes_ano = seleciona_mes_ano()

end = datetime.now()
print(end)


object_json = json.dumps(carros, indent=2, ensure_ascii=False)
with open('carrosACURA.json', 'w', encoding='utf-8') as file:
    file.write(object_json)
