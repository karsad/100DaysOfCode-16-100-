from re import search

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

total_articles_number = driver.find_elements(By.CSS_SELECTOR, '#articlecount a')
print("output:", total_articles_number[1].text)

# total_articles_number[0].click()
# most_viewed = driver.find_element(By.LINK_TEXT, "Most viewed pages")
# most_viewed.click()
# events = driver.find_ele

search = driver.find_element(By.NAME, "search")
search.send_keys("Asdfggasd", Keys.ENTER)

# driver.quit()
