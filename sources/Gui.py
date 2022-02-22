from cProfile import label
from tkinter import *
from tkinter.tix import WINDOW
from turtle import title
import GuiProperties as guiprop

# Configure Root
root = Tk()
root.configure(guiprop.root_configprop)


# Create Frames
search_frame = LabelFrame(root)
search_frame.configure(guiprop.searchframe_configprop)
search_frame.place(guiprop.searchframe_placeprop)

function_frame = LabelFrame(root)
function_frame.configure(guiprop.functionframe_configprop)
function_frame.place(guiprop.functionframe_placeprop)

display_frame = LabelFrame(root)
display_frame.configure(guiprop.displayframe_configprop)
display_frame.place(guiprop.displayframe_placeprop)


# Create widgets for search frame
back_button = Button(search_frame)
back_button.configure(guiprop.back_button_configprop)
back_button.place(guiprop.back_button_placeprop)

filter_entry = Entry(search_frame)
filter_entry.configure(guiprop.filter_entry_configprop)
filter_entry.place(guiprop.filter_entry_placeprop)

search_button = Button(search_frame)
search_button.configure(guiprop.search_button_configprop)
search_button.place(guiprop.search_button_placeprop)


# Create widgets for function frame
import_button = Button(function_frame)
import_button.configure(guiprop.import_button_configprop)
import_button.place(guiprop.import_button_placeprop)

export_button = Button(function_frame)
export_button.configure(guiprop.export_button_configprop)
export_button.place(guiprop.export_button_placeprop)


# Create widgets for display frame
display_textbox = Text(display_frame)
display_textbox.configure(guiprop.display_textbox_configprop)
display_textbox.configure(guiprop.display_textbox_placeprop)

root.mainloop()