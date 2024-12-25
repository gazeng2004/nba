from nba_api.stats.endpoints import playercareerstats, commonplayerinfo
import csv

"""
Want to incorporate height, weight, position into the nba stats 
Want to create a tinker outlines different stats points that can be inputed and show what player matches their respective roles
If possible, would want to produce a picture of each person

Afterward, think of ways to deal with ways with BIG outliers 
Should position be weighted more than other stats? How would I do that?
"""
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
    "PTS": 21,
    "Height": 22,
    "Position": 23,
    "Weight": 24
}

def weight(input_stat: dict, player_stats : list) -> int:
    weight : int = 0
    for stat, value in input_stat.items():

        if(stat == 'Position'):
            pos: str = player_stats[index[stat]]
            if(pos != value):
                weight += position_weight(pos, value)
        else:
            weight += abs(float(player_stats[index[stat]]) - value)
    return weight

def position_weight(player_pos, input_pos) -> int:
    player_list: list[str] = position_sep(player_pos)
    input_list: list[str] = position_sep(input_pos)
    
    try:
        for pos in player_list:
            for pos2 in input_list:
                if pos == pos2:
                    return 5 
        return 10
    except:
        return 10


def position_sep(pos) -> list[str]:
    if(len(pos) <= 7):
        return [pos]
    elif(pos[6] == '-'):
        return ["Forward", "Guard"]
    elif(pos[5] == '-'):
        return ["Center", "Forward"]

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

def id_reader(id: str) -> None:
    player_info = commonplayerinfo.CommonPlayerInfo(player_id = id)
    last_season = playercareerstats.PlayerCareerStats(player_id = id) 
    pdf = player_info.get_data_frames()[0]
    cdf = last_season.get_data_frames()[0].tail(1)
    print(pdf)
    print(cdf)

def question_num() -> int:
    try:
        input_value = float(input("Please type a number: "))
    except:
        return question_num()
    return input_value

def question_str(string: str) -> str:
    input_value = str(input("Please type a string: "))
    return input_value

def question() -> dict:
    input_dict = {}
    input_string = input("Please type a stat: ")
    while input_string in index:
        if(input_string == "Position"):
            input_value = question_str("string")
        else:
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
