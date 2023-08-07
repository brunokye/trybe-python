from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chrome = webdriver.Chrome()

response = chrome.get("https://www.google.com.br/")

search_input = chrome.find_element("name", "q")
search_input.send_keys("selenium")
search_input.send_keys(Keys.ENTER)
