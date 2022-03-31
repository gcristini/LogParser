import tkinter as tk
from Model.Model import Model
from View.View import View
from Controller.Controller import Controller
from Database.Database import Database

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        model = Model(Database())
        view = View(self)
        controller = Controller(model, view)

        view.setController(controller)


if __name__ == "__main__":
    app=App()
    app.mainloop()
    
    


