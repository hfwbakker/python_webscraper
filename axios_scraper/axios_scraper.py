import sys
from bs4 import BeautifulSoup
import requests

if len(sys.argv) == 1:
    target = 'https://www.axios.com/world'
    print(f"Target site: {target}")
else:
    target = str(sys.argv[1])
    print(f"Target site: {target}")

# html_text = requests.get('https://www.axios.com/world').text
html_text = requests.get(target).text

soup = BeautifulSoup(html_text, 'lxml')
articles = soup.find_all('div', class_ = "sc-1jy24uc-0 ehZYCh full gtm-content-click pt-20 up-to-sm:pt-12")

count = 1
for article in articles:
    header = article.find('a', class_ = 'title-link gtm-content-click')
    title = header.text
    text_body = article.find('div', class_ = "sc-31t5q3-7 sc-1jy24uc-2 bUgOWv up-to-sm:mb-4").text
    url = header.get('href')

    print(f"Article {count}: {title}\n")
    print(text_body + "\n")
    print(f"Link: {url}\n")
    print("-"*20 + "\n")
    count += 1


