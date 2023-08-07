from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()


def scrape(url):
    chrome.get(url)
    posts = []

    for post in chrome.find_elements(By.CLASS_NAME, 'post-outer'):
        new_item = dict()

        new_item['title'] = post.find_element(By.CLASS_NAME, 'entry-title') \
            .find_element(By.TAG_NAME, 'a').get_attribute('innerHTML')
        new_item['link'] = post.find_element(By.CLASS_NAME, 'entry-title') \
            .find_element(By.TAG_NAME, 'a').get_attribute('href')
        new_item['excerpt'] = (
            post.find_element(By.CLASS_NAME, 'entry-excerpt')
            .get_attribute('innerHTML')
        )

        posts.append(new_item)

    return posts


print(scrape('https://diolinux.com.br/'))
