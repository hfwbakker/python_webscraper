from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.axios.com/world').text
soup = BeautifulSoup(html_text, 'lxml')
articles = soup.find_all('amp-layout')
for article in articles:
    title = article.data-vars-headline

    print(title)



