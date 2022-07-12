import pytest

#pytest -v --driver Chrome --driver-path /path/to//chromedriver.exe

from selenium import webdriver #подключение библиотеки
driver = webdriver.Chrome() #получение объекта веб-драйвера для нужного браузера

driver = webdriver.Chrome()
driver.get('https://google.com')
