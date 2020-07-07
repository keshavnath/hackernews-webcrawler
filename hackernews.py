import requests, sys
from bs4 import BeautifulSoup as bs

feed=[]

def create_custom_feed(links, subtext, minpoints):

    for idx, item in enumerate(links):
        title=links[idx].getText()
        href=links[idx].get("href")
        vote=subtext[idx].select(".score")
        if len(vote):
            points=int(vote[0].getText().replace(" points", ""))
            if points>=minpoints:
                feed.append({"title":title, "link":href, "points":points})

def runthru(pgno, minpoints):

    for curno in range(1, pgno+1):     

        url="https://news.ycombinator.com/news?p=" + str(curno)
        res = requests.get(url)

        soup=bs(res.text, "html.parser")

        links=soup.select(".storylink")
        subtext=soup.select(".subtext")

        create_custom_feed(links, subtext, minpoints)

def generate(pages, minpoints):
    runthru(pages, minpoints)
    feed.sort(key = lambda k:k["points"], reverse=True)

def formalrun(custom_feed):
    for item in custom_feed:
        title=item.get("title")
        link=item.get("link")
        votes=item.get("points")
        print(f"Title : {title}")
        print(f"Link : {link}")
        print(f"Votes : {votes}")
        print("\n")

generate(int(sys.argv[1]), int(sys.argv[2]))
formalrun(feed)
