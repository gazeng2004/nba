import tkinter as tk


# This is a font that we'll use on all of the buttons, so we'll define it
# as a global constant.
DEFAULT_FONT = ('Helvetica', 12)
DEFAULT_FONT_SMALL = ('Helvetica', 8)


class SimpleLayoutApplication:
    def __init__(self):
        self._root = tk.Tk()

        self.pts = tk.DoubleVar(value = 0.0)
        self.reb = tk.DoubleVar(value = 0.0)
        self.ast = tk.DoubleVar(value = 0.0)
        self.blk = tk.DoubleVar(value = 0.0)
        self.height = tk.IntVar(value = 0)
        self.position = tk.StringVar(value = "")
        self.weight = tk.IntVar(value = 0)

        index: int = 0
        self._stats: list[str] = ["PTS", "REB", "AST", "BLK", "Height(inches)","Weight(lbs)", "Position"]
        for stat in self._stats:
            stat_label = self._make_label(self._root, stat)

            stat_label.grid(row = 0, column = index, padx = 0, pady = 0)
            index += 1

        index: int = 0
        self._stats_vars: list[tk.Variable] = [self.pts, self.reb, self.ast, self.blk, self.height, self.weight]
        for var in self._stats_vars:
            entry = self._make_entry(self._root, var)

            entry.grid(row = 1, column = index, padx = 0, pady = 0)
            index += 1
        
        opition = [
            "Guard",
            "Forward-Guard",
            "Forward",
            "Center-Forward",
            "Center"
        ]
        self.pos_entry = tk.OptionMenu(self._root, self.position, *opition)
        self.pos_entry.grid(row = 1, column = index, padx = 0, pady = 0)

    def _make_label(self, root : tk, text : str):
        return tk.Label(root, text = text, font = DEFAULT_FONT)

    def _make_entry(self, root : tk, var : tk.Variable):
        return tk.Entry(root, textvariable = var, font = DEFAULT_FONT_SMALL)


    def run(self):
        self._root.mainloop()



if __name__ == '__main__':
    SimpleLayoutApplication().run()