import tkinter
from tkinter import *
import tkinter.ttk

# A GUI based insolvency predictor, work in progress


class InsolvencyPredictor(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('Insolvency Predictor')
        self.state('zoomed')
        self.name_label = Label(self, text='Insolvency Predictor', bg='#31f1f7', width=140, height=2, font=10)
        self.name_label.place(x=0, y=0)


app = InsolvencyPredictor()
app.mainloop()
