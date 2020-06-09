#!/usr/bin/env python
import requests, re, json
from bs4 import BeautifulSoup
from collections import defaultdict

# function to parse html and return title and score dict
def parse_html(html):
    score_list = []
    game_list = []
    game_dict = defaultdict(list)

    parse = BeautifulSoup(html, 'html.parser')
    
    parse_ele = parse.find_all('a', class_='title')
    for i in parse_ele:
        
        element = str(i.find('h3'))
        game = re.findall(r'\w+', element)
        game = " ".join(game[1:-1])
        game_list.append(game)

    
    parse_clamp = parse.find_all(class_="browse-score-clamp")
    
    for i in parse_clamp:
        element = str(i.find(class_="metascore_w large game positive"))
        score = re.search('>(.*?)<', element).group(1)
        score_list.append(score)
    
    for k,val in enumerate(game_list):
        temp_dict = {'title': game_list[k], 'score': score_list[k]}
        game_dict[k].append(temp_dict)

    return game_dict
    
    
def to_json(game_dict):
    pass

def search():
    pass


def main():
    url="http://www.metacritic.com/game/playstation-4"
    raw=requests.get(url)
    html=raw.content

    game_dict=parse_html(html)

    to_json(game_dict)    


main()