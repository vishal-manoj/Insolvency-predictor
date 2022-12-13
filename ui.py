from tkinter import *


class Ui:
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.root.title('Insolvency Predictor')
        self.root.state('zoomed')
        self.root.name_label = Label(self.root, text='Insolvency Predictor', bg='#31f1f7', width=140, height=2, font=10)
        self.root.name_label.place(x=0, y=0)
        self.button_frame = Frame(self.root, height=740, width=300, highlightbackground='#31f1f7', highlightthickness=4)
        self.button_frame.place(x=0, y=50)
        self.display_frame = Frame(self.root, height=740, width=1235, highlightbackground='#31f1f7',
                                   highlightthickness=4)
        self.display_frame.place(x=300, y=50)
       






obj = Tk()
master = Ui(obj)
obj.mainloop()



