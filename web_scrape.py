import requests
from bs4 import BeautifulSoup as soup
from selenium import webdriver

url ="https://www.microcenter.com/product/608318/amd-ryzen-7-3700x-matisse-36ghz-8-core-am4-boxed-processor-with-wraith-prism-cooler"
web_r = requests.get(url)
web_soup = soup(web_r.text, 'html.parser')


chrome_path = r"C:\Users\zachery.perry\AppData\Local\Continuum\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get(url)
html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = soup(html, 'html.parser')


price = sel_soup.select("#pricing")
print(price)
