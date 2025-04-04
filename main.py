import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pickle
import time

# Configuraciones del navegador

options = Options()
options.add_argument('--windows-size=600,600')

service = Service(executable_path="chromedriver.exe")
driver = uc.Chrome(options=options, service=service)

profileButton = '//*[@id="app"]/div[2]/div/div/div[3]/div[1]/div[9]/a/button'
profileRepostsButton = '//*[@id="main-content-others_homepage"]/div/div[2]/div[1]/div/p[2]'
firstRepostedVideo = '//*[@id="main-content-others_homepage"]/div/div[2]/div[2]/div/div[1]'
repostButton = '//*[@id="icon-element-repost"]'


driver.get("https://www.tiktok.com/login/phone-or-email/email")

driver.implicitly_wait(5)

# driver.refresh()

# print("Inicia sesión como de costumbre")


def click(button):

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, button))
    )

    clickButton = driver.find_element(
        By.XPATH, button)

    clickButton.click()


cookies = pickle.load(open("cookies.pkl", "rb"))

for cookie in cookies:
    try:
        driver.add_cookie(cookie)
    except Exception as e:
        print(e)

driver.get("https://www.tiktok.com/@rreyeszx")

click(profileRepostsButton)
click(firstRepostedVideo)

outsideRepostedVideo = driver.find_element(
    By.XPATH, '/html')

contador = 0

while True:
    click(repostButton)
    with open("contador.txt", "w") as file:
        file.write(str(contador))
    print(f"Se han eliminado{contador} videos reposteados")
    time.sleep(0.1)
    outsideRepostedVideo.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.1)

# pickle.dump(cookies, open("cookie.pkl", "wb"))

# print(cookies)

# click(profileButton)
# click(profileRepostsButton)
# click(firstRepostedVideo)
