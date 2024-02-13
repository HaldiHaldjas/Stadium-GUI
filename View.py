from tkinter import *
from tkinter import messagebox
import tkinter.font as font


class View(Tk):

    #  kogu akna tegemine
    def __init__(self, controller):
        super().__init__()
        self.model = None
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

        # nupu loomine
        button1 = Button(frame1, text='Arvuta!', width='10', fg='black',
                         command=lambda: self.controller.calculations(entry1.get(), entry2.get()))
        button1.grid(row=3, column=4, padx=5, pady=5)
        return frame1

    def create_bottom_frame(self):
        frame2 = Frame(self, width=580, height=150, bg='lightyellow', padx=5, pady=5)
        frame2.pack(fill='both', expand=True)
        self.txt_results = Text(frame2, bg='white', fg='black')
        self.txt_results.grid(row=0, column=1, sticky="nsew")
        return frame2

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
        if r <= 0 or a <= 0 or r == type(str) or a == type(str):
            messagebox.showerror('Viga', 'Sisesta vaid positiivseid arve!')
            return

        self.txt_results.delete(1.0, END)
        self.txt_results.insert(END, f"Raadius: {r}\n")
        self.txt_results.insert(END, f"Küljepikkus: {a}\n")
        self.txt_results.insert(END, f"Ümbermõõt: {perimeter}\n")
        self.txt_results.insert(END, f"Pindala: {area}\n")
        self.txt_results.insert(END, f"Keskosa pindala: {area_rec}\n")

    def on_close(self):
        self.destroy()
