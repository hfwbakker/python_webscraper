"""
- https://www.timeoutshanghai.com/FoodDrink.html
- loop over <a> tag with "class="tile__anchor_link" get href and title (or <div> class="tile__content"?)
- call function to get first few lines of text and date from url
- y/n to print whole article

"""
soup_function.find_all(articles)

for article class articles
    title = a.get("title")
    description = p.get.text 
    url = a.get("href")

    ans input("get article? y/n")
    if ans = y
        scraping_function(url)
    else
        continue // return "carrying on"