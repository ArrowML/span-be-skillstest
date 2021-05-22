import fileinput
from functools import reduce
from typing import Dict, List

def controller():
    buffer = []
    process = [parseGameInput, calcScores, sortRankings, outputRankings]
    for line in fileinput.input():
        if line.strip() == 'show ranking':
            reduce(lambda x, y: y(x), process, buffer) 
        else:
            if line.strip() != '':
                buffer.append(line)
    else:
        reduce(lambda x, y: y(x), process, buffer)

# Parse input into base teams dictionary and create result list    
def parseGameInput(buffer: List):
    games_list = []
    for games in buffer:       
        results = games.split(', ')
        team1 = results[0].rsplit(' ', 1)
        team2 = results[1].rsplit(' ', 1)
        game = {"team1_name":team1[0], "team1_score":int(team1[1]), "team2_name":team2[0], "team2_score":int(team2[1].strip('\n'))}
        games_list.append(game)
    return games_list 

# calculate scores per team
def calcScores(games: List):
    score = {'win': 3, 'draw': 1}
    team_scores = {}
    for game in games:
        #set base values
        if game['team1_name'] not in team_scores:
            team_scores[game['team1_name']] = 0
        if game['team2_name'] not in team_scores:
            team_scores[game['team2_name']] = 0   
        # add scores
        if game['team1_score'] > game['team2_score']:
            team_scores[game['team1_name']] += score['win']
        elif game['team2_score'] > game['team1_score']:
            team_scores[game['team2_name']] += score['win']
        elif game['team1_score'] == game['team2_score']:
            team_scores[game['team1_name']] += score['draw']
            team_scores[game['team2_name']] += score['draw']     
    return team_scores

def sortRankings(team_scores: Dict):
    ranking = sorted(team_scores.items(), key=lambda x: (-x[1], x[0]))
    return ranking

# output ordered ranking table
def outputRankings(sorted_results: List):
    for i in range(len(sorted_results)):
        print( "%d. %s, %d pts" %((i+1), sorted_results[i][0], sorted_results[i][1] ))
    quit()    

if __name__ == "__main__":
    controller()