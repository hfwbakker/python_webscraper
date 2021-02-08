# python_webscraper

progress exercise:

https://www.youtube.com/watch?v=XVv6mJpFOb0&feature=youtu.be&ab_channel=freeCodeCamp.org

at 39:00 min.

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

Next up:
- Print articles of a certain category
- Print articles from older pages as well. There is a link at the bottom of the page called "older articles" or something that loads previous day articles and so on. Figure out a way to specify how many times you want to go back and print it. Perhaps by making another script that calls this scraper on each page?
- Get the contents from the URL ("go deeper") for each article as well.
- Some pretty printing perhaps?