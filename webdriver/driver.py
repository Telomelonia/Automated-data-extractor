from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

service = Service(executable_path='webdriver\chromedriver-win64\chromedriver.exe')
options = webdriver.ChromeOptions()
def url_opener(url):
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    time.sleep(5)
    driver.quit()