import requests
from bs4 import BeautifulSoup
import Historyinnerlink

def Page(url,num):

        req = requests.get(url)
        htmL = BeautifulSoup(req.text, "html.parser")

        tags = htmL.find('div', {'class': 'article-wrapper archive-default'})
        # all link on different pages.
        for linktag in tags.findAll('h2', {'class': 'entry-title'}):
            for link in linktag.findAll('a'):
                url = link.get('href')
                # calling function to scrape data from each single--link
                num =Historyinnerlink.scrap(url,num)
        #finding next page link
        pages = tags.find('div',{'class':'archive-pagination'})
        current_page = int(pages.find('span',{'class':'page-numbers current'}).text)
        current_page+=1
        #sending next page link
        Page(f"https://www.gyandarpan.com/category/glorious-history/page/{current_page}",num)

Page("https://www.gyandarpan.com/category/glorious-history/",1)
