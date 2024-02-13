from tkinter import *
from tkinter import ttk, simpledialog, messagebox
import tkinter.font as font
from tkinter.ttk import Treeview


class View(Tk):

    #  kogu akna tegemine
    def __init__(self, controller):
        super().__init__()
        self.txt_results = None
        self.btn_calculate = None
        self.controller = controller
        self.__width = 600
        self.__height = 300
        self.default_font = font.Font(family='Helvetica', size=14)

        #   Akna omadused
        self.title('Staadioni GUI')
        self.center_window(self.__width, self.__height)

        #  frame'ide loomine
        self.top_frame = self.create_top_frame()
        self.bottom_frame = self.create_bottom_frame()
        # self.txt_results = None

        #  todo enter klahv tööle

    def main(self):
        self.mainloop()

    #  aken ekraani keskele
    def center_window(self, width, height):
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')
        # self.geometry('600x300')

    def create_top_frame(self):
        frame1 = Frame(self, width=600, height=100, bg='lightyellow')
        frame1.pack(fill='both', expand=True)

        lbl_radius = Label(frame1, width=15, bg='lightyellow', fg='black', text='Raadius:')
        lbl_side_len = Label(frame1, width=15, bg='lightyellow', fg='black', text='Küljepikkus:')
        lbl_radius.grid(row=1, column=1, padx=5, pady=5)
        lbl_side_len.grid(row=3, column=1, padx=5, pady=5)

        entry1 = Entry(frame1, width=30, bg='white')
        entry2 = Entry(frame1, width=30, bg='white')
        entry1.grid(row=1, column=2, padx=5, pady=5)
        entry2.grid(row=3, column=2, padx=5, pady=5)
        entry1.focus()

        # Create buttons
        button1 = Button(frame1, text='Arvuta!', width='10', fg='black',
                         command=lambda: self.controller.calculations(float(entry1.get()), float(entry2.get())))
        button1.grid(row=3, column=4, padx=5, pady=5)
        return frame1

    def create_bottom_frame(self):
        frame2 = Frame(self, width=580, height=150, bg='lightyellow', padx=5, pady=5)
        frame2.pack(fill='both', expand=True)
        self.txt_results = Text(frame2, bg='white', fg='black')
        self.txt_results.grid(row=0, column=1, sticky="nsew")
        return frame2

    # def create_frame_widgets(self):
    #
    #     #  nupud
    #     btn_calc_perimeter = Button(self.top_frame, text='Arvuta staadioni ümbermõõt', font=self.default_font,
    #                                 command=self.controller.stadium_calculations(self.perimeter), state=DISABLED)
    #     btn_calc_area = Button(self.top_frame, text='Arvuta staadioni pindala', font=self.default_font,
    #                            command=self.controller.stadium_calculations(self.area), state=DISABLED)
    #     btn_calc_rec = Button(self.top_frame, text='Arvuta staadioni keskosa pindala', font=self.default_font,
    #                           command=self.controller.calculations(self.area_rec), state=DISABLED)
    #
    #     #  sildid staadioni raadius ja küljepikkus
    #     lbl_radius = Label(self.top_frame, text='Sisesta staadioni raadius', font=self.default_font)
    #     lbl_side_len = Label(self.top_frame, text='Sisesta staadioni küljepikkus', font=self.default_font)
    #     lbl_radius.grid(row=1, column=1, padx= 5, pady=5)
    #     lbl_side_len.grid(row=2, column=1, padx=5, pady=5)
    #
    #     #  mõõtude sisestamine
    #     radius_entry = Entry(self.top_frame, font=self.default_font, state=DISABLED)
    #     side_len_entry = Entry(self.top_frame, font=self.default_font, state=DISABLED)
    #     radius_entry.grid(row=1, column=2, padx=5, pady=5)
    #     radius_entry.grid(row=2, column=2, padx=5, pady=5)

    #  vidinate loomine
    # (self.btn_calculate, self.radius_entry,
    # self.side_length_entry, self.text_box) = self.create_top_frame()
    def create_pop_up_window(self):
        top = Toplevel(self)
        top.title('Viga')
        top_width = 400
        top_height = 150
        x = (top.winfo_screenwidth() // 2) - (top_width // 2)
        y = (top.winfo_screenheight() // 2) - (top_height // 2)
        top.geometry(f'{top_width}x{top_height}+{x}+{y}')
        top.resizable(False, False)
        top.grab_set()
        top.focus()
        frame = Frame(top)
        frame.pack(fill=BOTH, expand=True)
        return frame

    def show_results(self, r, a, perimeter, area, area_rec):
        if r <= 0 or a <= 0:
            messagebox.showerror('Viga', 'Sisesta vaid positiivseid arve!')
            return

        self.txt_results.delete(1.0, END)
        self.txt_results.insert(END, f"Raadius: {r}\n")
        self.txt_results.insert(END, f"Küljepikkus: {a}\n")
        self.txt_results.insert(END, f"Ümbermõõt: {perimeter}\n")
        self.txt_results.insert(END, f"Pindala: {area}\n")
        self.txt_results.insert(END, f"Keskosa pindala: {area_rec}\n")

    # def show_results(self, frame, data):
    #     my_table = Treeview(frame)
    #     my_table['columns'] = ('Andmed', 'Tulemused')
    #     my_table['rows'] = ('Raadius', 'Küljepikkus', 'Ümbermõõt', 'Pindala', 'Keskosa pindala')
    #     my_table.column(width=0, stretch=NO)
    #     my_table.column('Raadius', anchor=LEFT)
    #     my_table.column('Küljepikkus', anchor=LEFT)
    #     my_table.column('Ümbermõõt', anchor=LEFT)
    #     my_table.column('Pindala', anchor=LEFT)
    #     my_table.column('Keskosa pindala', anchor=LEFT)
    #
    #     my_table.insert(parent='', values=(self.radius_entry, self.side_len_entry, self.perimeter,
    #                                        self.area, self.area_rec))
    #     my_table.pack(fill=BOTH, expand=True)

    def on_close(self):
        self.destroy()
