import tkinter as tk
from nba_stats import comparision
from nba_api.stats.endpoints import playercareerstats, commonplayerinfo
import pandas as pd

# This is a font that we'll use on all of the buttons, so we'll define it
# as a global constant.
DEFAULT_FONT = ('Helvetica', 12)
DEFAULT_FONT_SMALL = ('Helvetica', 8)


class SimpleLayoutApplication:
    def __init__(self):
        self._root = tk.Tk()
        self._root.geometry("900x400")

        self.pts = tk.DoubleVar(value = 0.0)
        self.reb = tk.DoubleVar(value = 0.0)
        self.ast = tk.DoubleVar(value = 0.0)
        self.blk = tk.DoubleVar(value = 0.0)
        self.height = tk.IntVar(value = 0)
        self.position = tk.StringVar(value = "")
        self.weight = tk.IntVar(value = 0)
        self.display = tk.StringVar(value = "Input Stats")

        self._label_maker()
        index = self._entry_maker()
        self._pos_entry_make(index)
        self._button_maker_command("Input", 2, 3, self.info_getter)
        self._display = tk.Label(
            self._root, 
            height = 10, 
            width = 60, 
            font = DEFAULT_FONT, 
            textvariable = self.display,
            bg = "lightblue",
            highlightthickness = 2,
            highlightbackground = "black",
        )
        self._display.grid(row = 4, column = 0, columnspan = 6)

    def _button_maker_command(self, text, row, column, command) -> tk.Button:
        button = tk.Button(
            master = self._root,
            text = text, 
            font = DEFAULT_FONT,
            command = command
        )

        button.grid(
            row = row, column = column,
            sticky = tk.N + tk.S + tk.W + tk.E
        )
        
        return button

    def info_getter(self):
        stat_list = {}
        if self.check(self.pts.get()):
            stat_list["PTS"] = self.pts.get()
            self.pts.set(0.0)
        if self.check(self.reb.get()):
            stat_list["REB"] = self.reb.get()
            self.reb.set(0.0)
        if self.check(self.ast.get()):
            stat_list["AST"] = self.ast.get()
            self.ast.set(0.0)
        if self.check(self.blk.get()):
            stat_list["BLK"] = self.blk.get()
            self.blk.set(0.0)
        if self.check(self.height.get()):
            stat_list["Height"] = self.height.get()
            self.height.set(0)
        if self.check(self.position.get()):
            stat_list["Position"] = self.position.get()
            self.position.set("")
        if self.check(self.weight.get()):
            stat_list["Weight"] = self.weight.get()
            self.weight.set(0)
        
        id = comparision.reader(stat_list)
        output_str: str = self.display_stat(id)
        self.display.set(output_str)
    
    def display_stat(self, id: str) -> str:
        player_info = commonplayerinfo.CommonPlayerInfo(player_id = id)
        last_season = playercareerstats.PlayerCareerStats(player_id = id)
        pdf: pd.DataFrame = player_info.get_data_frames()[0]
        cdf: pd.DataFrame = last_season.get_data_frames()[0]
        tail = cdf.tail(1)

        output_str: str = pdf.loc[0, "FIRST_NAME"] + " " + pdf.loc[0, "LAST_NAME"]
        output_str += " " + str(tail.loc[len(cdf) - 1, "PLAYER_AGE"])
        return output_str

    def check(self, stat):
        stat_set = {0.0, 0, ""}
        if stat in stat_set:
            return False
        return True

    def _label_maker(self) -> None:
        index: int = 0
        self._stats: list[str] = ["PTS", "REB", "AST", "BLK", "Height(inches)","Weight(lbs)", "Position"]
        for stat in self._stats:
            stat_label = self._make_label(self._root, stat)

            stat_label.grid(row = 0, column = index, padx = 0, pady = 0)
            index += 1
    
    def _entry_maker(self) -> int:
        index: int = 0
        self._stats_vars: list[tk.Variable] = [self.pts, self.reb, self.ast, self.blk, self.height, self.weight]
        for var in self._stats_vars:
            entry = self._make_entry(self._root, var)

            entry.grid(row = 1, column = index, padx = 0, pady = 0)
            index += 1
        return index

    def _make_label(self, root : tk, text : str):
        return tk.Label(root, text = text, font = DEFAULT_FONT)

    def _make_entry(self, root : tk, var : tk.Variable):
        return tk.Entry(root, textvariable = var, font = DEFAULT_FONT_SMALL)
    
    def _pos_entry_make(self, index):
        opition = [
            "Guard",
            "Forward-Guard",
            "Forward",
            "Center-Forward",
            "Center"
        ]
        self.pos_entry = tk.OptionMenu(self._root, self.position, *opition)
        self.pos_entry.grid(row = 1, column = index, padx = 0, pady = 0)

    def run(self):
        self._root.mainloop()




if __name__ == '__main__':
    SimpleLayoutApplication().run()