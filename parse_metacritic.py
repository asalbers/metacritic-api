import requests, re, json
from bs4 import BeautifulSoup
from collections import defaultdict
from flask import Flask, request

def parse_html():
    # Parses html input by searching for classes.
    # Creates two lists after parsing then joins the two lists in a nested dictionary.
    
    url = "http://www.metacritic.com/game/playstation-4"
    raw = requests.get(url)
    html = raw.content

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
        json_output = ''
        for key, val in game_dict.items():
            output = json.dumps(val, indent =4)
            json_output += output
        return json_output
    else:
        json_output = json.dumps(game_dict, indent =4)
        return json_output 

def search(query, game_dict):
    # Compares the inputted query against values in the dictionary and returns whether it matches or not
    result = ''
    for key, val in game_dict.items():
        for key2, val2 in val.items():
            if val2.lower() == query.lower():
                result = key

    return game_dict[result]

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return "{ web_api: 0.1.0 }"

@app.route('/games', methods = ["GET"])
def all_games():
    game_dict = parse_html()
    formatted = to_json(game_dict)
    return formatted

@app.route('/games/<game>', methods = ["GET"])
def query_games(game):
    game_dict = parse_html()
    query = search(str(game), game_dict)
    formatted = to_json(query)
    return formatted


app.run(host = '0.0.0.0', port = '8080', debug = True)
