from parsel import Selector
import requests


URL_BASE = "http://books.toscrape.com/catalogue/"
next_page_url = 'page-1.html'

while next_page_url:

    response = requests.get(URL_BASE + next_page_url)
    selector = Selector(text=response.text)
    # print(selector)

    for product in selector.css(".product_pod"):
        title = product.css("h3 a::attr(title)").get()
        price = product.css(".price_color::text").re_first(r"£\d+\.\d{2}")
        print(title, price)

        detail_href = product.css("h3 a::attr(href)").get()
        detail_page_url = URL_BASE + detail_href

        detail_response = requests.get(detail_page_url)
        detail_selector = Selector(text=detail_response.text)

        descr = detail_selector.css("#product_description ~ p::text").get()

        suffix = "...more"

        if descr.endswith(suffix):
            descr = descr[:-len(suffix)]

        print(f"{descr}\n")

    next_page_url = selector.css(".next a::attr(href)").get()
