from msilib.schema import Extension
from tkinter import filedialog

class Controller:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        return

    def search_in_log(self):
        pass

    def export_log(self):
        pass
        
    def import_log(self, filePath: str):        
        self._view.update_display_textbox(text=self._model.import_log(filePath).readlines(), append = False)

        pass




# def search_button_callback():
#     return

# def back_button_callback():
#     return



# def export_button_callback():
#     return