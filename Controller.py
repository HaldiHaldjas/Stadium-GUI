from tkinter import simpledialog

from Model import Model
from View import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def calculations(self, radius, side_length):
        self.model.calculations(radius, side_length)
        self.view.show_results(self.model.radius,
                               self.model.side_len,
                               self.model.perimeter,
                               self.model.area,
                               self.model.area_rec)

