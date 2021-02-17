from bs4 import BeautifulSoup
import requests
import pprint
from urllib.request import Request, urlopen


def get_article(x):
    req = Request(x, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'lxml')
    articles = soup.find_all('div', class_="article__content")
    paragraphs = articles[0].find_all('p')

    user_choice = input("print article? y/n\n> ")
    if user_choice == "y":
        print("you opted to print")
        for paragraph in paragraphs:
            print(paragraph.text + "\n")
    else:
        print("you opted not to print")


def scrape_politico(search_term=' ', target_url='https://www.politico.eu/'):
    print(f"called scrape_politico with {search_term} on {target_url}")
    req = Request(target_url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'lxml')
    articles = soup.find_all('div', class_="card__content")
    count = 1
    for article in articles:
        header = article.find('a')
        title = header.text.strip()
        url = header.get('href')

        if search_term in header or search_term in title:
            print(f"Article {count}: {title}")
            print(f"URL: {url}\n")
            count += 1
            get_article(url)
        
        else:
            print(f"Skipping article {count}: {title[0:30]}...\n")
            print("-"*20 + "\n")
            count += 1

    print("That's all. Bye!")


def user_selection():
    search_for_selection = str(input("\n Filter for what? \n> "))
    choice = str(input("\nCustom URL (press RETURN for default Politico homepage) \n>"))
    if choice == '':
        scrape_politico(search_for_selection)
    else:
        scrape_politico(choice, search_for_selection)

user_selection()