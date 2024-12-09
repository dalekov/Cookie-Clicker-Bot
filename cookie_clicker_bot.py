from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
timeout = time.time() + 60*5  # 5 minutes from now


upgrades = {
    "Cursor": "buyCursor",
    "Grandma": "buyGrandma",
    "Factory": "buyFactory",
    "Mine": "buyMine",
    "Shipment": "buyShipment",
    "Alchemy Lab": "buyAlchemy lab",
    "Portal": "buyPortal",
    "Time Machine": "buyTime machine",
}

def get_price(element):
    element_ = driver.find_element(By.ID, value=element)
    price_text = element_.text.split(' - ')[1].split('\n')[0].replace(',', '')
    return int(price_text)

# Endlessly clicking on the cookie
while True:
    cookie.click()
    # Stop after 5 mins:
    if time.time() > timeout:
        break

    # Get current money:
    try:
        money = int(driver.find_element(By.ID, value="money").text.replace(',',''))

        affordable_upgrades = [element_id for name, element_id in upgrades.items() if money >= get_price(element_id)]
        if affordable_upgrades:
            affordable_upgrades.sort(key=get_price, reverse=True)
            upgrade = driver.find_element(By.ID, value=affordable_upgrades[0])
            upgrade.click()
    except Exception as e:
        print(f"Error: {e}")