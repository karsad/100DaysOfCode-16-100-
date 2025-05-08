from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
URL2 = "https://appbrewery.github.io/instant_pot/"
URL3 = "https://python.org"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# driver.get(URL2)
#
# price_whole = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# name = driver.find_element(By.ID,"productTitle")
# print(f"{name.text}\nCurrent price is: ${price_whole.text}.{price_fraction.text} !")
# driver.quit()


driver.get(URL3)

dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
events = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu a")

output = {num: {"time": dates[num].text, "name": events[num].text} for num in range(len(dates))}
print(output)
driver.quit()
