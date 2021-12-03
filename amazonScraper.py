from selenium import webdriver
from selenium.webdriver.common.by import By
import json


def captureDetails():
    specKeys = driver.find_elements(By.XPATH, "//td[contains(@class, 'a-span3')]")
    specValues = driver.find_elements(By.XPATH, "//td[contains(@class, 'a-span9')]")
    specs = {}
    for i in range(len(specKeys)):
        specs[specKeys[i].text] = specValues[i].text
    driver.back()
    return specs

def execute():
   
    phoneslist = driver.find_elements(By.XPATH, "//span[contains(@class, 'a-size-medium a-color-base')]")
    prices = driver.find_elements(By.XPATH, "//span[contains(@class, 'a-price-whole')]")
    phoneLink = driver.find_elements(By.XPATH, "//a[contains(@class, 'a-size-base a-link-normal a-text-normal')]")

    allPhones = []
    allPrices = []
    allSpecs = []

    for phone in phoneslist:
        allPhones.append(phone.text)
        

    for price in prices:
        allPrices.append(price.text)

    for link in phoneLink:
        link.click()
        allSpecs.append(captureDetails())

    # final = zip(allPhones, allPrices)

    driver.find_element(By.XPATH, "//li[contains(@class, 'a-last')]").click()
    return [allPhones, allPrices, allSpecs]

driver=webdriver.Chrome(executable_path="/home/navgurukul/Desktop/selenium/chromedriver")
driver.maximize_window()
driver.get("https://amazon.in")
driver.implicitly_wait(10)
# print(captureDetails())
inputSearch = driver.find_element(By.XPATH, "//input[contains(@id, 'twotabsearchtextbox')]")
inputSearch.send_keys("samsung phones")
driver.find_element(By.XPATH, "//input[contains(@id, 'nav-search-submit-button')]").click()
driver.find_element(By.XPATH, "//span[text()='Samsung']").click()
lists = []
for i in range(1):
    lists.append({i:execute()})
    print(execute())
with open("mydata.json", 'w') as f:
    json.dump(lists, f, indent=4)

driver.close()