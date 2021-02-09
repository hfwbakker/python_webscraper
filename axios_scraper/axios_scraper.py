import sys
from bs4 import BeautifulSoup
import requests

###### imput argument logic ######
if len(sys.argv) == 3:
    target = str(sys.argv[1])
    search_for = str(sys.argv[2])
    print(f"\nTarget site: {target}, filtering for {search_for}.\n\n")
elif len(sys.argv) == 2:
    target = str(sys.argv[1])
    print(f"\nTarget site: {target}, no filter.")
else: 
    target = 'https://www.axios.com/world'
    print(f"\nTarget site: {target}\n\n")

###### get text from URL function ######
def get_article(x):
    html_text = requests.get(x).text
    soup = BeautifulSoup(html_text, 'lxml')
    text_content = soup.find('div', class_ = "b0w77w-0 gyJiUn mt-12 mb-20 sm:mt-20 gtm-story-text p").text

    user_choice = input("print article? y/n")
    if user_choice == "y":
        print("printing text content of link\n")
        print(text_content)
    else:
        print("you elected not to print.")


###### beatiful soup ######
html_text = requests.get(target).text
soup = BeautifulSoup(html_text, 'lxml')
articles = soup.find_all('div', class_ = "sc-1jy24uc-0 ehZYCh full gtm-content-click pt-20 up-to-sm:pt-12")

count = 1
for article in articles:
    header = article.find('a', class_ = 'title-link gtm-content-click')
    title = header.text
    text_body = article.find('div', class_ = "sc-31t5q3-7 sc-1jy24uc-2 bUgOWv up-to-sm:mb-4").text
    url = header.get('href')

    if search_for in header or search_for in title or search_for in text_body:
        print(f"Article {count}: {title}\n")
        print(text_body + "\n")
        print(f"Link: {url}\n")
        get_article(url)
        print("-"*20 + "\n")
        count += 1
    else:
        print(f"Skipping article {count}: {title[0:30]}...\n")
        print("-"*20 + "\n")
        count += 1

