# Este código utiliza a biblioteca Selenium para: abrir o Firefox, 
# acessar o site "https://selenium.dev", contar quantas vezes a palavra "Selenium" 
# aparece no código-fonte da página e exibir o resultado no terminal. 
# Em seguida, aguarda antes de fechar o navegador.

# Bibliotecas necessárias
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox() 
driver.get("https://selenium.dev")

texto_da_pagina = driver.page_source # Obtém o código-fonte da página usando o string driver.page_source
palavra_alvo = "Selenium" # Escolhe a palavra que deseja contar no código-fonte da página

numero_de_ocorrencias = texto_da_pagina.count(palavra_alvo) # .count é um método de string que conta quantas vezes a palavra    
# aparece no código-fonte da página
print(f"A palavra '{palavra_alvo}' aparece {numero_de_ocorrencias} vezes nesta página.") # terminal

sleep(5)  # Aguarda 5 segundos antes de fechar o navegador
driver.quit()

