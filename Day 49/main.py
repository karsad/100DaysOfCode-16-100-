from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

load_dotenv()

URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
URL_LOGIN = "https://www.linkedin.com/login?emailAddress=&fromSignIn=&fromSignIn=true&session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%2F%3Ff_LF%3Df_AL%26geoId%3D102257491%26keywords%3Dpython%2520developer%26location%3DLondon%252C%2520England%252C%2520United%2520Kingdom%26redirect%3Dfalse%26position%3D1%26pageNum%3D0&trk=public_jobs_nav-header-signin"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(URL_LOGIN)
while len(driver.find_elements(By.ID, "username")) == 0: pass
driver.find_element(By.ID, "username").send_keys(os.environ.get("LOGIN"))
driver.find_element(By.ID, "password").send_keys(os.environ.get("PASS"))
driver.find_element(By.CSS_SELECTOR, ".btn__primary--large.from__button--floating").click()

while len(driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")) == 0: pass
time.sleep(2)
jobs_list = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
print(len(jobs_list))

for job in jobs_list:
    while len(driver.find_elements(By.CLASS_NAME, "jobs-save-button__text")) == 0: pass
    driver.find_element(By.CLASS_NAME, "jobs-save-button__text").click()
    time.sleep(1)
    job.click()