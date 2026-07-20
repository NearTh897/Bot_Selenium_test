# Este código utiliza a biblioteca Selenium para: abrir o Firefox, 
# acessar o site "https://selenium.dev", contar quantas vezes a palavra "Selenium" 
# aparece no código-fonte da página e exibir o resultado no terminal. 
# Em seguida, aguarda antes de fechar o navegador.

# Bibliotecas necessárias
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from time import sleep

service = Service('/home/theo/Área de trabalho/Selenium/Bot_Selenium_test/geckodriver') # Caminho para o driver do Firefox (geckodriver)
driver = webdriver.Firefox(service=service)

driver.get("https://selenium.dev") # Acessa o site "https://selenium.dev"

texto_da_pagina = driver.page_source # Obtém o código-fonte da página usando o string driver.page_source
palavra_alvo = "Selenium" # Escolhe a palavra que deseja contar no código-fonte da página

numero_de_ocorrencias = texto_da_pagina.count(palavra_alvo) # .count é um método de string que conta quantas vezes a palavra    
# aparece no código-fonte da página
print(f"A palavra '{palavra_alvo}' aparece {numero_de_ocorrencias} vezes nesta página.") # terminal

sleep(5)  # Aguarda 5 segundos antes de fechar o navegador
driver.quit()


# Infelizmente, não é possível executar este código aqui, 
# pois ele requer a instalação do Selenium e do driver do Firefox,
# além de um ambiente gráfico para abrir o navegador. 
# No entanto, você pode executar este código em seu próprio ambiente local, 
# desde que tenha o Selenium e o driver do Firefox instalados corretamente.
# O código requer o Selenium instalado e possui direitos e licença para uso.

# Com Venv, ele dá erros dentro do sistema.