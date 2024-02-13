import math
from tkinter import messagebox


class Model:
    def __init__(self):
        self.__radius = 0
        self.__side_len = 0
        self.__perimeter = 0
        self.__area = 0
        self.__area_rec = 0

    @property
    def radius(self):
        return self.__radius

    @property
    def side_len(self):
        return self.__side_len

    @property
    def perimeter(self):
        return self.__perimeter

    @property
    def area(self):
        return self.__area

    @property
    def area_rec(self):
        return self.__area_rec

    # @staticmethod
    # def is_number(user_input):
    #     try:
    #         float(user_input)
    #         return True
    #     except ValueError:
    #         print("Error: Input values must be numeric")
    #         return False

    @staticmethod
    def is_number(user_input):
        try:
            nbr = float(user_input)
            if nbr <= 0:
                return False
            return True
        except ValueError:
            return False

    def calculations(self, r, a):
        is_r_numeric = self.is_number(r)
        is_a_numeric = self.is_number(a)

        if not (is_r_numeric and is_a_numeric):
            messagebox.showerror("Viga!", "Raadius ja küljepikkus on vigased.")
            return

        r = float(r)
        a = float(a)
        if r <= 0 or a <= 0:
            messagebox.showerror("Viga!", "Raadius ja küljepikkus peavad olema positiivsed arvud.")

        p = math.pi
        perimeter = 2 * (p * r + a)
        area = p * r ** 2 + 2 * r * a
        area_rec = 2 * r * a
        self.__perimeter = perimeter
        self.__area = area
        self.__area_rec = area_rec
        self.__radius = r
        self.__side_len = a
        self.view.show_results(perimeter, area, area_rec, r, a)
