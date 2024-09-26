from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pandas as pd
import time


target_url = [
    'https://www.instagram.com/',
    'https://www.instagram.com/',
    'https://www.instagram.com/',
    'https://www.instagram.com/',
    'https://www.instagram.com/',
    'https://www.instagram.com/',
    'https://www.instagram.com/'

]
test_target_url = [
    'https://www.instagram.com/',

]
# open driver
s = Service('chromedriver-win64\chromedriver.exe')
options = Options()
driver = webdriver.Chrome(service=s, options=options)

# buka url
driver.get(test_target_url[0])
wait = WebDriverWait(driver, timeout=10)
element = wait.until(EC.presence_of_element_located(
    (By.CLASS_NAME, 'g47SY')))

# extract data


# simpan data ke dalam csv
