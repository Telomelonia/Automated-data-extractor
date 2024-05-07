from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import PyPDF2

service = Service(executable_path='webdriver\chromedriver-win64\chromedriver.exe')
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)
url = "https://www.sciencedirect.com/science/article/pii/S0924013698004506"

if url.endswith('.pdf'):
    pdf_reader = PyPDF2.PdfFileReader(driver.current_url)
    
    # Extract text from each page
    for page in pdf_reader.pages:
        print(page.extractText())
else:        
    driver.get(url)
    time.sleep(5)
    
    # Get the HTML source of the page
    html_source = driver.page_source

    # Parse the HTML source using BeautifulSoup
    soup = BeautifulSoup(html_source, 'html.parser')

    # Example: Print the title of the page
    print("Title:", soup.text)
    driver.quit()
