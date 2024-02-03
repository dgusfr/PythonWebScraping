from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

edge_driver_path = 'msedgedriver.exe'

edge_service = Service(edge_driver_path)

edge_options = Options()
edge_options.add_argument('window-size=400,800')

navegador = webdriver.Edge(service=edge_service, options=edge_options)

navegador.get('https://www.airbnb.com')

sleep(2)

input_place = navegador.find_element(By.TAG_NAME, 'input')
input_place.send_keys('São Paulo')
input_place.send_keys(Keys.ENTER)

sleep(0.5)

button_stay = navegador.find_element(By.CSS_SELECTOR, 'button > img')
button_stay.click()

sleep(0.5)

nextButton = navegador.find_elements(By.TAG_NAME, 'button')[-1]
nextButton.click()

sleep(0.5)

adultButton = navegador.find_elements(By.CSS_SELECTOR, 'button > span > svg > path[d="m2 16h28m-14-14v28"]')[0]
adultButton.click()
sleep(1)
adultButton.click()
sleep(1)

searchButton = navegador.find_elements(By.TAG_NAME, 'button')[-1]
searchButton.click()

sleep(4)

page_content = navegador.page_source

site = BeautifulSoup(page_content, 'html.parser')

print(site.prettify())

navegador.quit()
