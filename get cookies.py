import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pickle

# Configuraciones del navegador

options = Options()
options.add_argument('--windows-size=600,600')

service = Service(executable_path="chromedriver.exe")
driver = uc.Chrome(options=options, service=service)

profileButton = '//*[@id="app"]/div[2]/div/div/div[3]/div[1]/div[9]/a/button'

driver.get("https://www.tiktok.com/login/phone-or-email/email")

WebDriverWait(driver, 300).until(
    EC.presence_of_element_located(
        (By.XPATH, profileButton))
)

cookies = driver.get_cookies()

pickle.dump(cookies, open("cookies.pkl", "wb"))
