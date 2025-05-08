from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://orteil.dashnet.org/cookieclicker/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)
driver.implicitly_wait(1)
consent = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/button[1]/p")
consent.click()
driver.implicitly_wait(1)
language = driver.find_element(By.ID, "langSelect-PL")
language.click()
cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')

while True:
    cookie.click()
