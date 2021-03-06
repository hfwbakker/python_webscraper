# python_webscraper

axios_scraper.py project:

NEXT UP:
- Add a GUI linking all scraper scripts, possibly using flask or PySimpgleGUI (check https://www.youtube.com/watch?v=NZMTWBpLUa4)
- Add scrapers for F&B trend watch websites (smartshanghai? CNN travel perhaps?)


KNOWN BUGS:

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

Added pprint for article printing. Not a great solution but enough for now.

Installed Flask for the virtualenv to see if I can use it to make a GUI. Idea is to have some menu where i can select which website to scrape and I will just start adding customized scraping scripts for each. Axios scraper is 99% there now. Next up is a Flask deep dive.

--- Saturday February 13th ---
Built a basic Flask app. The plan:
    - use import to import axios_scraper.py functions
    - create a seperate /axios page
    - call the customized script there and display text to browser and get input through keys
    - rinse and repeat for other files as well 

This approach stil just outputs to terminal instead of browser. Not sure how to fix yet.

Someone told me the following: Flask is a reasonable tool, and I should look into "jsonify" (jsonify the program output) and "jinja2", claiming that any decent Flask tutorial should cover this. Flask + json deepdive continues...

Also: add scrapers for F&B trend watch websites (smartshanghai? CNN travel perhaps?)

--- Sunday February 14th ---
Removed a lot of useless files. Did some more research on Flask and think I finally found a good source: https://realpython.com/python-web-applications/ tomorrow should try to build a basic app with this. 

--- Wednesday February 17th ---
Fixed a bug where the div with the main text was addressed with the wrong class in the get_article() function, causing a NoneType error. Fixed it for now by adding this other class identifier. Not sure if this means there are many of they change over time. Should look in to if this is a thing for automatically generated websites? Possibly an effect of using "React" + "CSS modules".

Did the realpython tutorial. More studying of Flask needed. Perhaps should look into GUI option mentioned in same article

Added politico scraper, works pretty much the same as the Axios one.

--- Saturday February 20th ---
Fixed a bug where politico scraper threw an error on mac (something related to urllib). Solution: run "Install Certificates" command in Mac applications Python 3.9 folder.

--- Monday February 22nd ---
Did some tinkering with openpyxl. Refer to excel_python folder in python for loop code that can put all scraper output into an excel sheet. Suggest I make a "excel_it()" function that can be called on request when finishing scraping a page that allows to e.g. put titles + urls + dates in an excel sheet. Probably should include a test that notifies user if an excel sheet by that name already exists and will possible be overridden.

Next question would be if openpyxl can be used to read form an excel sheet.

--- Tuesday February 23rd ---
Included openpyxl in axios_scraper.py. Article name + url are now saved to an excel file named output.xlsx when chosing so on prompt. Now need to refine output sheet and prevent accidental overwrites when scraping more than one page.

--- Wednesday February 24th ---
Added column width to script. Script will now also check if there is already an output file by that name and save it to a different name (output0, output1, etc). 
Experimented with PySimpleGUI.