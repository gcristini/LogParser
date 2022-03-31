from msilib.schema import Extension
from tkinter import filedialog

class Controller:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        return

    def filter_log(self, words:list):
        self._view.update_display_textbox(text=self._model.filter_log(words), append=False)        

    def export_log(self):
        pass
        
    def import_log(self, filePath: str):
        self._model.clear_log_data()
        self._view.update_display_textbox(text=self._model.import_log(filePath), append = False)
            
    def go_back(self):
        log = self._model.get_previous_filtered_log()
        # print (log)
        if log is not None:
            self._view.update_display_textbox(log, append=False)       


# def search_button_callback():
#     return

# def back_button_callback():
#     return



# def export_button_callback():
#     return