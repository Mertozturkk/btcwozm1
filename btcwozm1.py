"""
10.09.2021
Author: Mert Öztürk
Purpose: Web Scraping with python From the puzzle game The Mini Crossword
from the game page of the New York Times
We want to see all hint to daily puzzles
"""
import logging
import json
import requests
from bs4 import BeautifulSoup as bs

# we use logging library to keep program logs
# First: Creating new logger
# Second: İt's record at info level
# Third: Creating a log file
# Fourth: LOG_FORMAT-how the data is saved in the file
# Fifth: Let's specify the recording format to our file
# Lastly: let's set our file as a logger 
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
LOG_FILE = logging.FileHandler('logfile.log')
LOG_FORMAT = logging.Formatter('%(asctime)s - %(name)s [%(levelname)s]: %(message)s')
LOG_FILE.setFormatter(LOG_FORMAT)
LOGGER.addHandler(LOG_FILE)

LOGGER.info('Application started working')
try: #running inside a block for a possible error condition
    URL = 'https://www.nytimes.com/crosswords/game/mini'
    r = requests.get(URL)
    LOGGER.info('Requesting URL: https://www.nytimes.com/crosswords/game/mini')
    soup = bs(r.content,'html.parser')
except:
    print("An unexpected error has occurred!")
    LOGGER.info("An error occurred while requesting")

def hint_hunter():
    """
    This function performs data extraction, listing data, saving in JSON format
    and printing the desired data to the screen.
    """
    hint_set1 = []
    hint_set2 = []
    text_ = soup.find_all("span",attrs={"class":"Clue-text--3lZl7"})
    # we access the relevant tags through the link we use
    try:
        for link in text_:
            hint_set1.append((link.text))
        # using a list method We add it to our list called hint_set1

        num_ = soup.find_all("span",attrs={"class":"Clue-label--2IdMY"}) # same process for the numbers
        for link in num_:
            hint_set2.append((link.text))
        LOGGER.info('Content gathered')
    except:
        LOGGER.info('Error occurred while accessing data')

    json_ = {hint_set1[i]: hint_set2[i] for i in range(len(hint_set1))}
    # we create a dictionary from the obtained lists,

    with open("hint.json","a") as file:
        json.dump(json_, file) # open an JSON file and save it
    LOGGER.info('JSON file created,')

    print('=== Across ===')
    for i in range(len(hint_set1)): # a small loop to print hints on the screen
        print('{}. {}'.format(hint_set2[i],hint_set1[i]))
        if i == 4 :
            print("=== Down ===")
    LOGGER.info('Data is saved and printed on the screen')

if __name__== "__main__":
    hint_hunter()