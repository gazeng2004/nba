from nba_api.stats.endpoints import playercareerstats, commonplayerinfo
import csv
import pandas as pd
import math

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

class NbaNN:
    """
    file = '2024-2025nbaStats.csv'
    """
    def __init__(self, file):
        self.lines = pd.read_csv(file)

    def weight(self, input_stats):
        pass

    def printer(self):
        print(self.lines["Position"].unique())
    
if __name__ == "__main__":
    one = NbaNN('2024-2025nbaStats.csv')
    one.printer()