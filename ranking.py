import fileinput
from typing import Dict, List

games_list = []
teams_list = {}
score = {'win': 3, 'draw': 1}

def controller():
    buffer = []
    for line in fileinput.input():
        if line.strip() == 'show table':
            parseGameInput(buffer)    
        else:
            if line.strip() != '':
                buffer.append(line)
    else:
        parseGameInput(buffer) 

# Parse input into dictionary    
def parseGameInput(buffer: List):  
    for games in buffer:       
        results = games.split(', ')
        team1 = results[0].rsplit(' ', 1)
        team2 = results[1].rsplit(' ', 1)
        game = {"team1_name":team1[0], "team1_score":int(team1[1]), "team2_name":team2[0], "team2_score":int(team2[1].strip('\n'))}
        games_list.append(game)
        teams_list[team1[0]] = 0
        teams_list[team2[0]] = 0
    calcScores(games_list)

def calcScores(games: Dict):
    for game in games:
        if game['team1_score'] > game['team2_score']:
            teams_list[game['team1_name']] += score['win']
        elif game['team2_score'] > game['team1_score']:
            teams_list[game['team1_name']] += score['win']
        elif game['team1_score'] == game['team2_score']:
            teams_list[game['team1_name']] += score['draw']
            teams_list[game['team2_name']] += score['draw']    
    outputRankings(teams_list)

def outputRankings(ranking: List):
    ranking = sorted(teams_list.items(), key=lambda x: (-x[1], x[0]))
    for i in range(len(ranking)):
        print( "%d. %s, %d pts" %((i+1), ranking[i][0], ranking[i][1] ))
    quit()    


controller()