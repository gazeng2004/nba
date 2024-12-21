from nba_api.stats.endpoints import playercareerstats, commonplayerinfo
import csv

index = {
    "id" :  0,
    "Age" : 1,
    "GP" : 2,
    "Min": 3,
    "FGM": 4,
    "FGA": 5,
    "FG_PCT": 6,
    "FG3M": 7,
    "FG3A": 8,
    "FG_PCT": 9,
    "FTM" : 10,
    "FTA" : 11,
    "FT_PCT" : 12,
    "OREB": 13,
    "DREB": 14,
    "REB": 15,
    "AST": 16,
    "STL": 17,
    "BLK": 18,
    "TOV": 19,
    "PF": 20,
    "PTS": 21
}

def weight(input_stat: dict, player_stats : list):
    weight : int = 0
    for stat, value in input_stat.items():
        weight += abs(float(player_stats[index[stat]]) - value)
    return weight

   
def old_reader(value : float, stat : str):
    dict = {}
    with open('2024-2025nbaStats.csv', mode = 'r') as file:
        next(file)
        csvFile = csv.reader(file)
        for lines in csvFile:
            dict[abs(float(lines[index[stat]]) - value)] = lines[0]

    return dict[min(dict)]

def reader(input_dict : dict):
    dict = {}
    with open('2024-2025nbaStats.csv', mode = 'r') as file:
        next(file)
        csvFile = csv.reader(file)
        for lines in csvFile:
            dict[weight(input_dict, lines)] = lines[0]

    return dict[min(dict)]

def id_reader(id):
    player_info = commonplayerinfo.CommonPlayerInfo(player_id = id)
    last_season = playercareerstats.PlayerCareerStats(player_id = id) 
    pdf = player_info.get_data_frames()[0]
    cdf = last_season.get_data_frames()[0].tail(1)
    print(pdf)
    print(cdf)

def question_num():
    try:
        input_value = float(input("Please type a number: "))
    except:
        return question_num()
    return input_value

def question():
    input_dict = {}
    input_string = input("Please type a stat: ")
    while input_string in index:
        input_value = question_num()
        input_dict[input_string] = input_value
        input_string = input("Please type a stat: ")
    return input_dict

if __name__ == '__main__':
    value = question()
    print(value)
    id : str = reader(value)
    id_reader(id)
    '''
    home = input("Please input a integer")
    word : str = input("Please input a string")
    id : str = reader(float(home), word)
    id_reader(id)
    '''
