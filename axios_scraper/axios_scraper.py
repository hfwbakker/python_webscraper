from bs4 import BeautifulSoup
import requests
import pprint

target = ' '
search_for = ' '

########################################
###### get text from URL function ######
########################################
def get_article(x):
    html_text = requests.get(x).text
    soup = BeautifulSoup(html_text, 'lxml')
    text_content = soup.find('div', class_ = "b0w77w-0 gyJiUn mt-12 mb-20 sm:mt-20 gtm-story-text p").text

    user_choice = input("print article? y/n\n> ")
    if user_choice == "y":
        print("printing text content of link\n")
        pprint.pprint(text_content)
    else:
        print("you elected not to print.")

##################################
###### main webscrape logic ######
##################################
def scrape_it(search_for=' ', target='https://www.axios.com/world'):
    print(f"called scrape_it with {search_for} on {target}")
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
            print(text_body[0:300] + "...\n")
            print(f"Link: {url}\n")
            get_article(url)
            print("-"*20 + "\n")
            count += 1
        else:
            print(f"Skipping article {count}: {title[0:30]}...\n")
            print("-"*20 + "\n")
            count += 1

    #### go to next page logic block ####
    try:
        next_page = soup.find('a', class_="sc-31t5q3-10 kHAPjX sc-19f8cds-0 gXiJMM gtm-content-click").get('href')
    except AttributeError:
        nav_links = soup.find_all('a', class_="gtm-content-link no-underline hover:text-accent-blue-shade hover:underline flex items-center space-x-4 text-soft-black-core")
        next_page = nav_links[-1].get('href')
    except:
        print("No link for next page found.")
        print("See you next time!")
        exit(0)
    choice = input("Scrape next page? (y/n)\n> ")
    if choice == "y":
        scrape_it(search_for, next_page)
    else:
        print("see you next time!")
        exit(0)
    ########################################


############################
##### user input logic #####
############################
def user_selection():
    search_for_selection = str(input("\n Filter for what? \n> "))
    choice = str(input("\nCustom URL (press RETURN for default Axios.com/world) \n>"))
    if choice == '':
        scrape_it(search_for_selection)
    else:
        scrape_it(choice, search_for_selection)


###############################
##### program starts here #####
###############################
user_selection()
