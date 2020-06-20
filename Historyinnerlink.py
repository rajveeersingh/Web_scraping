import requests
from bs4 import BeautifulSoup

def title(name):
    '''Function to find title of the
    every single topic '''
    title1 = name.find('div', {'class': 'post-lead'})
    title = title1.find('h1')
    titl = (title.text).strip().replace('/','_')
    return titl

def scrap(url,num):
    req = requests.get(f'{url}')
    htmL = BeautifulSoup(req.text, "html.parser")
    #For finding the title
    div1 = htmL.find('div',{'class':'container'})
    #For extracting the data of every single topics
    div2 = div1.find('div',{'class':'entry-content'})
    # calling function title for finding of title of the topic
    titl = title(div1)
    data = div2.text
    # writing data to the .txt files in History_txt directory
    with open(f'History_txt/{num}_{titl}.txt', 'w') as file:
        file.write(f'{data}')
    return num+1

