import tkinter as tk

class Scrollbar_Example:
    def __init__(self):
        self.window = tk.Tk()

        self.scrollbar = tk.Scrollbar(self.window, orient=tk.HORIZONTAL)
        self.scrollbar.pack(side="bottom", fill="x")

        self.text = tk.Text(self.window,
                            wrap = "none",
                            xscrollcommand=self.scrollbar.set)
        
        self.text.insert("end", str(dir(tk.Scrollbar)))
        self.text.pack(side="top", fill="x")

        self.scrollbar.config(command=self.text.xview)

        self.window.mainloop()


if __name__ == '__main__':
    app = Scrollbar_Example()  