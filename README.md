# python_webscraper

progress exercise:

https://www.youtube.com/watch?v=XVv6mJpFOb0&feature=youtu.be&ab_channel=freeCodeCamp.org

at 39:00 min.

Virtualenv:
source webscraper_env/bin/activate

axios_scraper.py project:


LOG:
--- Sunday February 7th ---
Started working on a Axios webscraper. The plan and results so far:
    * step 0: continue the course...
    * step 1: print titles + text on any given axios page
        - can select articles themselves but cant select the titles yet..
    * step 2: print titles + text of only articles in a specific category
    * step 3: get the content from the links too ("go deeper" section)
    * step 4: define how far back to go (e.g. today, but also yesterday and day before)
    * step 5 make input convenient (command line args?)

--- Monday February 8th ---
Basic functionality achieved! Can now call any axios page link with argv (default is set to 'axios/world'), and it will print all articles titles, text, and URL to full article.

--- Tuesday February 9th ---
Added .gitignore, created virtual environment, prettified axios scraper print-out a bit.

Early evening sesh: Can now enter a argument to filter for from command line.  Articles that don't contain this term will only print "skipping article". Also added a function that prints the text from the "go deeper" link. Perhaps good to add a choice where you see the abstract first and then the question "print article y/n" or something? -> done and done. Maybe refine choice question a bit but works otherwise.

Evening session pt 2: Relevant abstracts are displayed first, user can select y/n to print article or skip to next. At the end of page user can select y/n to start scraping the next page. Next page function does not yet work well because the next page link is not the same on every site. Need to write some logic that selects whatever link exists on that page. However, problem with creating a seperate function is scope -> "search_for" value gets lost upon going to next page. Need to see how to fix that.

--- Friday February 12th ---
Now correctly keeps going to next page upon request. Next up improving readability of printing.


Next up:
- Some pretty printing perhaps?
- Same thing for other websites...
- GUI?