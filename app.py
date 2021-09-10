import requests
from bs4 import BeautifulSoup as bs


url = 'https://www.nytimes.com/crosswords/game/mini'

r = requests.get(url)
soup = bs(r.content,'html.parser')


hint_set1 = []
hint_set2 = []

def hint_hunter():
    
    """
    hint_title = soup.find_all("h3",attrs={"class":"ClueList-title--1-3oW"})
    for link in hint_title:
        titles.append((link.text))
    """

    c = soup.find_all("span",attrs={"class":"Clue-text--3lZl7"})
    for link in c:
        hint_set1.append((link.text))



    tr = soup.find_all("span",attrs={"class":"Clue-label--2IdMY"})
    for link in tr:
        hint_set2.append((link.text))


    print('=== Across ===')
    for i in range(len(hint_set1)):
        print('{}. {}'.format(hint_set2[i],hint_set1[i]))
        if i ==4 :
            print("=== Down ===")
        
if __name__== "__main__":
    hint_hunter()