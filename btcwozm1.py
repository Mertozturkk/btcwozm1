"""
10.09.2021

Author: Mert Öztürk
Purpose: Web Scraping with python From the puzzle game The Mini Crossword from the game page of the New York Times. We want to see all hint to daily puzzles

"""






import requests
from bs4 import BeautifulSoup as bs
import json


url = 'https://www.nytimes.com/crosswords/game/mini'

r = requests.get(url)
soup = bs(r.content,'html.parser')

def hint_hunter():
    hint_set1 = []
    hint_set2 = []
    
    text_ = soup.find_all("span",attrs={"class":"Clue-text--3lZl7"})    #we access the relevant tags through the link we use
    for link in text_:
        hint_set1.append((link.text))                                   #using a list method We add it to our list called hint_set1

    num_ = soup.find_all("span",attrs={"class":"Clue-label--2IdMY"})    #same process for the numbers
    for link in num_:
        hint_set2.append((link.text))

    json_ ={hint_set1[i]: hint_set2[i] for i in range(len(hint_set1))}  #we create a dictionary from the obtained lists,  
    with open("hint.json","a") as f:
        json.dump(json_, f)                                             # open an JSON file and save it 

    print('=== Across ===')
    for i in range(len(hint_set1)):                                     #a small loop to print hints on the screen
        print('{}. {}'.format(hint_set2[i],hint_set1[i]))
        if i ==4 :
            print("=== Down ===")
        
if __name__== "__main__":
    hint_hunter()


