# THIS IS PROGRAM TO TAKE INFO FROM WEB USING BEAUTIFUL SOUP4 LIBRARY
# download library of beautiful soup install : pip install beautifulsoup4 
import requests
from bs4 import BeautifulSoup
import pprint
res = requests.get('https://news.ycombinator.com/')
# print(res)
soup = BeautifulSoup(res.text,'html.parser')
# WE CAN NOW MANUPLATE AND WE ADD METHOD TO AFTER SOUP . MATHOD WE CAN TAKE THE INFOR WHATEVER WE WANT 
links = soup.select('.titleline') 
votes= soup.select('.score')
subtext =  soup.select('.subtext')


def sort_stories_by_votes(hnlist):
    return sorted(hnlist,key = lambda k: k['votes'])



def create_cistom_hn(links, votes):
    hn=[]
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')    
        if len(vote):        
            points = int(vote[0].getText().replace('points',''))
            if points > 99:
                print(points)
                hn.append({'title':title,'link':href,'votes':points})
    return hn

pprint.pprint(create_cistom_hn(links, subtext))