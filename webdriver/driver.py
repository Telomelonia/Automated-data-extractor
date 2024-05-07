from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

service = Service(executable_path='webdriver\chromedriver-win64\chromedriver.exe')
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.sciencedirect.com/science/article/pii/S1359646222005486")
time.sleep(5)
# Get the HTML source of the page
html_source = driver.page_source

# Parse the HTML source using BeautifulSoup
soup = BeautifulSoup(html_source, 'html.parser')

# Example: Print the title of the page
print("Title:", soup.title)
driver.quit()