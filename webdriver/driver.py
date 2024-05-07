from io import BytesIO
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import requests
from PyPDF2 import PdfReader
service = Service(executable_path='webdriver\chromedriver-win64\chromedriver.exe')
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)
url = "https://www.researchgate.net/profile/Praswasti-Wulan/publication/316360082_Finding_an_Optimum_Period_of_Oxidative_Heat_Treatment_on_SS_316_Catalyst_for_Nanocarbon_Production_from_LDPE_Plastic_Waste/links/593e12d3458515e39875c7fd/Finding-an-Optimum-Period-of-Oxidative-Heat-Treatment-on-SS-316-Catalyst-for-Nanocarbon-Production-from-LDPE-Plastic-Waste.pdf?_sg%5B0%5D=started_experiment_milestone&origin=journalDetail&_rtd=e30%3D"
driver.get(url)
time.sleep(8)
if "pdf" in driver.current_url.lower():
    pass
else:        
    # Get the HTML source of the page
    html_source = driver.page_source

    # Parse the HTML source using BeautifulSoup
    soup = BeautifulSoup(html_source, 'html.parser')

    # Example: Print the title of the page
    print("Title:", soup.text)
driver.quit()
