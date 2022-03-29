from msilib.schema import Extension
from cProfile import label
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter.tix import WINDOW
from turtle import title
from View import ViewProperties
import os

class View():
    def __init__(self, parent):        

        # Create View
        self._createView(parent)

        # Set the controller
        self.controller = None
        return

    def _createView(self, parent):
        # Configure Root
        self.root = parent                
        self.root.configure(ViewProperties.root_configprop)
        self.root.resizable(False, False)


        # Create Frames
        self.search_frame = LabelFrame(self.root)
        self.search_frame.configure(ViewProperties.searchframe_configprop)
        self.search_frame.place(ViewProperties.searchframe_placeprop)

        self.function_frame = LabelFrame(self.root)
        self.function_frame.configure(ViewProperties.functionframe_configprop)
        self.function_frame.place(ViewProperties.functionframe_placeprop)

        self.display_frame = LabelFrame(self.root)
        self.display_frame.configure(ViewProperties.displayframe_configprop)
        self.display_frame.place(ViewProperties.displayframe_placeprop)


        # Create widgets for search frame
        self.back_button = Button(self.search_frame)
        self.back_button.configure(ViewProperties.back_button_configprop)
        self.back_button.place(ViewProperties.back_button_placeprop)

        self.filter_entry = Entry(self.search_frame)
        self.filter_entry.configure(ViewProperties.filter_entry_configprop)
        self.filter_entry.place(ViewProperties.filter_entry_placeprop)

        self.search_button = Button(self.search_frame)
        self.search_button.configure(ViewProperties.search_button_configprop, command=self._filter_log)
        self.search_button.place(ViewProperties.search_button_placeprop)


        # Create widgets for function frame
        self.import_button = Button(self.function_frame)
        self.import_button.configure(ViewProperties.import_button_configprop, command=self._import_log)
        self.import_button.place(ViewProperties.import_button_placeprop)     
           

        self.export_button = Button(self.function_frame)
        self.export_button.configure(ViewProperties.export_button_configprop)
        self.export_button.place(ViewProperties.export_button_placeprop)


        # Create widgets for display frame
        self.scrollbar_x = Scrollbar(self.display_frame)
        self.scrollbar_x.config(ViewProperties.display_scrollbar_x_configprop)
        self.scrollbar_x.pack(ViewProperties.display_scrollbar_x_packprop)

        self.scrollbar_y = Scrollbar(self.display_frame)
        self.scrollbar_y.config(ViewProperties.display_scrollbar_y_configprop)
        self.scrollbar_y.pack(ViewProperties.display_scrollbar_y_packprop)

        self.display_textbox = Text(self.display_frame)
        self.display_textbox.configure(ViewProperties.display_textbox_configprop, xscrollcommand=self.scrollbar_x.set, yscrollcommand=self.scrollbar_y.set)        
        self.display_textbox.pack(ViewProperties.display_textbox_packprop)

        self.scrollbar_x.config(command=self.display_textbox.xview)
        self.scrollbar_y.config(command=self.display_textbox.yview)
        return

    ### Callbacks
    def _import_log(self):
        if (self._controller):
            self._controller.import_log(filedialog.askopenfilename())
        return

    def _export_log(self):
        if (self._controller):
            pass

    def _filter_log(self):
        if (self._controller):
            filter_words = self.filter_entry.get().split(";")            
            self._controller.filter_log(filter_words)
            pass

    def setController(self, controller):
        self._controller=controller



    def update_display_textbox(self, text:str = "", append:bool = False):
        self.display_textbox.configure(state=NORMAL)
        
        if append:
            pass
        else:
            self.display_textbox.delete("1.0","end")   
            self.display_textbox.insert(INSERT, text)        
            self.display_textbox.configure(state=DISABLED)
            
            
        return



if __name__ == "__main__":
    from View import ViewProperties
    view = View()
    