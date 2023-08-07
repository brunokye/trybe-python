import requests
from bs4 import BeautifulSoup


def get_html_soup(url):
    page = requests.get(url)
    html_page = page.text

    soup = BeautifulSoup(html_page, "html.parser")
    soup.prettify()
    return soup


def get_page_news(soup):
    news = []

    for post in soup.find_all(
        "article", {"class": "tec--card tec--card--medium"}
    ):
        item = {}

        info_div = post.find("div", {"class": "tec--card__info"})
        if info_div:
            item["tag"] = info_div.a.string

        title_element = post.find("h3", {"class": "tec--card__title"})
        if title_element:
            item["title"] = title_element.a.string
            item["link"] = title_element.a["href"]

        date_div = post.find(
            "div", {"class": "tec--timestamp__item z--font-semibold"}
        )
        if date_div:
            item["date"] = date_div.string

        time_div = post.find("div", {"class": "z--truncate z-flex-1"})
        if time_div:
            item["time"] = time_div.string

        news.append(item)

    return news


def get_next_page(soup_page):
    try:
        return soup_page.find(
            "a",
            {"class": "tec--btn"},
        )["href"]
    except TypeError:
        return None


def scrape_all(url):
    all_news = []

    while get_next_page(get_html_soup(url)) is not None:
        print(get_next_page(get_html_soup(url)))

        all_news.extend(get_page_news(get_html_soup(url)))
        url = get_next_page(get_html_soup(url))

    return all_news


print(scrape_all("https://www.tecmundo.com.br/novidades?page=11888"))
