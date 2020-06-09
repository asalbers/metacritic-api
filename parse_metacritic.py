#!/usr/bin/env python
import requests, re, json
from bs4 import BeautifulSoup
from collections import defaultdict

def parse_html(html):
    # Parses html input by searching for classes.
    # Creates two lists after parsing then joins the two lists in a nested dictionary.

    score_list = []
    game_list = []
    game_dict = defaultdict(dict)

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
        game_dict[k] = temp_dict

    return game_dict
    
    
def to_json(game_dict):
    # Takes the inputted dictionary and outputs it to the expected json format

    if len(game_dict) > 2:
        temp_dict = {}
        for key, val in game_dict.items():
            json_output = json.dumps(val, indent =4)
            return json_object
    else:
        json_object = json.dumps(game_dict, indent =4)
        return json_output 

def search(query, game_dict):
    # Compares the inputted query against values in the dictionary and returns whether it matches or not
    
    result = ''
    for key, val in game_dict.items():
        for key2, val2 in val.items():
            if val2 == query:
                result = key

    return game_dict[result]

def main():
    url="http://www.metacritic.com/game/playstation-4"
    raw=requests.get(url)
    html=raw.content

    game_dict=parse_html(html)

    #to_json(game_dict)
    query = search('Nioh 2', game_dict)
    to_json(query)


main()