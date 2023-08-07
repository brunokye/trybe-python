from selenium import webdriver
from selenium.webdriver.common.by import By


chrome = webdriver.Chrome()


def scrape(url):
    chrome.get(url)

    print(
        chrome.find_element(By.CLASS_NAME, 'text').get_attribute('innerHTML')
    )


scrape('https://quotes.toscrape.com/')
