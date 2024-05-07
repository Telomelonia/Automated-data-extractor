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
url = "https://www.researchgate.net/profile/Gianender-Kajal/publication/364335455_Process_Parameter_Selection_for_Optimizing_the_Weld_Pool_Geometry_of_Stainless_Steel_SS_202_SS_316_of_the_TIG_Welding_using_Taguchi_Method/links/634ac4b576e39959d6c50807/Process-Parameter-Selection-for-Optimizing-the-Weld-Pool-Geometry-of-Stainless-Steel-SS-202-SS-316-of-the-TIG-Welding-using-Taguchi-Method.pdf"
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
    print("texts:", soup.text)
driver.quit()
