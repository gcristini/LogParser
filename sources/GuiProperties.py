import os
from tkinter import PhotoImage
from tkinter.ttk import *

# *******************************************
# *************    CONSTANTS    ************* 
# *******************************************

# ROOT
__ROOT_TITLE = "LogParser"
__ROOT_WIDTH = 800
__ROOT_HEIGHT= 800

__ROOT_RELMARGIN_TOP = 0.1
__ROOT_RELMARGIN_BOTTOM = 0.05
__ROOT_RELMARGIN_LEFT = 0.03
__ROOT_RELMARGIN_RIGHT = 0.03

__ROOT_BACKGROUND = "#2d2d2d"
__FRAME_BACKGROUND = "#2d2d2d"

root_configprop = {    
    "width": __ROOT_WIDTH,
    "height" : __ROOT_HEIGHT,
    "background" : __ROOT_BACKGROUND
}


# SEARCH FRAME
__SEARCH_FRAME_RELX = __ROOT_RELMARGIN_LEFT
__SEARCH_FRAME_RELY = __ROOT_RELMARGIN_TOP
__SEARCH_FRAME_RELHEIGHT = 0.09
__SEARCH_FRAME_RELWIDTH = 0.8

__SEARCH_FRAME_MARGIN_TOP = 0.15
__SEARCH_FRAME_MARGIN_BOTTOM = 0.15
__SEARCH_FRAME_MARGIN_LEFT = 0.03
__SEARCH_FRAME_MARGIN_RIGHT = 0.03
__SEARCH_FRAME_INTERSPACE = 0.01

searchframe_configprop = {
    "text": "Search",
    "background": __FRAME_BACKGROUND,
    "foreground": "#EFEFEF"
}
searchframe_placeprop = {
    "relx": __SEARCH_FRAME_RELX, 
    "rely": __SEARCH_FRAME_RELY, 
    "relheight": __SEARCH_FRAME_RELHEIGHT,
    "relwidth": __SEARCH_FRAME_RELWIDTH
}


# FUNCTION FRAME
__FUNCTION_FRAME_RELX = __ROOT_RELMARGIN_LEFT + __SEARCH_FRAME_RELWIDTH + 0.02
__FUNCTION_FRAME_RELY = __ROOT_RELMARGIN_TOP + 0.01
__FUNCTION_FRAME_RELHEIGHT = 0.1
__FUNCTION_FRAME_RELWIDTH = 1-__FUNCTION_FRAME_RELX-__ROOT_RELMARGIN_RIGHT

__FUNCTION_FRAME_MARGIN_TOP = 0.15
__FUNCTION_FRAME_MARGIN_BOTTOM = 0.15
__FUNCTION_FRAME_MARGIN_LEFT = 0.03
__FUNCTION_FRAME_MARGIN_RIGHT = 0.03
__FUNCTION_FRAME_INTERSPACE = 0.05

functionframe_configprop= {
    "background": __FRAME_BACKGROUND
}
functionframe_placeprop = {
    "relx": __FUNCTION_FRAME_RELX,
    "rely": __FUNCTION_FRAME_RELY, 
    "relheight":__FUNCTION_FRAME_RELHEIGHT,
    "relwidth": __FUNCTION_FRAME_RELWIDTH
}


# DISPLAY FRAME
__DISPLAY_FRAME_RELX = __ROOT_RELMARGIN_LEFT
__DISPLAY_FRAME_RELY = 0.03 +  max(__SEARCH_FRAME_RELHEIGHT + __FUNCTION_FRAME_RELY, __FUNCTION_FRAME_RELHEIGHT + __FUNCTION_FRAME_RELY)
__DISPLAY_FRAME_RELHEIGHT = 1 - __DISPLAY_FRAME_RELY - __ROOT_RELMARGIN_BOTTOM
__DISPLAY_FRAME_RELWIDTH = 1 - __ROOT_RELMARGIN_LEFT - __ROOT_RELMARGIN_RIGHT

displayframe_configprop= {
    "background": __FRAME_BACKGROUND
}
displayframe_placeprop = {
    "relx": __DISPLAY_FRAME_RELX, 
    "rely": __DISPLAY_FRAME_RELY, 
    "relheight": __DISPLAY_FRAME_RELHEIGHT,
    "relwidth": __DISPLAY_FRAME_RELWIDTH
}

# BACK BUTTON
__BACK_BUTTON_RELX = __SEARCH_FRAME_MARGIN_LEFT
__BACK_BUTTON_RELY = __SEARCH_FRAME_MARGIN_TOP
__BACK_BUTTON_RELHEIGHT = 1 - __SEARCH_FRAME_MARGIN_TOP - __SEARCH_FRAME_MARGIN_BOTTOM
__BACK_BUTTON_RELWIDTH = 0.07

back_button_configprop = {}
back_button_placeprop = {
    # "image" : __BACK_BUTTON_PATH
    "relx": __BACK_BUTTON_RELX, 
    "rely": __BACK_BUTTON_RELY, 
    "relheight": __BACK_BUTTON_RELHEIGHT,
    "relwidth": __BACK_BUTTON_RELWIDTH
}

# SEARCH BUTTON
__SEARCH_BUTTON_RELWIDTH = 0.07
__SEARCH_BUTTON_RELX = 1 - __SEARCH_FRAME_MARGIN_RIGHT - __SEARCH_BUTTON_RELWIDTH
__SEARCH_BUTTON_RELY = __SEARCH_FRAME_MARGIN_TOP
__SEARCH_BUTTON_RELHEIGHT = 1 - __SEARCH_FRAME_MARGIN_TOP - __SEARCH_FRAME_MARGIN_BOTTOM

search_button_configprop = {}
search_button_placeprop = {
    # "image" : __SEARCH_BUTTON_PATH
    "relx": __SEARCH_BUTTON_RELX, 
    "rely": __SEARCH_BUTTON_RELY, 
    "relheight": __SEARCH_BUTTON_RELHEIGHT,
    "relwidth": __SEARCH_BUTTON_RELWIDTH
}

# FILTER ENTRY
__FILTER_ENTRY_RELX = __SEARCH_FRAME_MARGIN_LEFT + __BACK_BUTTON_RELWIDTH + __SEARCH_FRAME_INTERSPACE
__FILTER_ENTRY_RELY = __SEARCH_FRAME_MARGIN_TOP
__FILTER_ENTRY_RELHEIGHT = 1 - __SEARCH_FRAME_MARGIN_TOP - __SEARCH_FRAME_MARGIN_BOTTOM - 0.02
__FILTER_ENTRY_RELWIDTH = 1 - __SEARCH_FRAME_MARGIN_LEFT - __SEARCH_FRAME_MARGIN_RIGHT - __BACK_BUTTON_RELWIDTH - __SEARCH_BUTTON_RELWIDTH - 2*__SEARCH_FRAME_INTERSPACE -0.002

filter_entry_configprop = {}
filter_entry_placeprop = {        
    "relx": __FILTER_ENTRY_RELX, 
    "rely": __FILTER_ENTRY_RELY, 
    "relheight": __FILTER_ENTRY_RELHEIGHT,
    "relwidth": __FILTER_ENTRY_RELWIDTH
}


import_button_configprop = {
    "text": "import"
}
import_button_placeprop = {
    "relx": __FUNCTION_FRAME_MARGIN_LEFT,
    "rely": __FUNCTION_FRAME_MARGIN_TOP,
    "relheight": 0.5 - __FUNCTION_FRAME_MARGIN_TOP - (__FUNCTION_FRAME_INTERSPACE/2),
    "relwidth": 1 - __FUNCTION_FRAME_MARGIN_LEFT - __FUNCTION_FRAME_MARGIN_RIGHT
}

export_button_configprop = {
    "text": "export"
}
export_button_placeprop = {
    "relx": __FUNCTION_FRAME_MARGIN_LEFT,
    "rely": 0.5 + __FUNCTION_FRAME_INTERSPACE/2,
    "relheight": 0.5 - __FUNCTION_FRAME_MARGIN_BOTTOM - (__FUNCTION_FRAME_INTERSPACE/2),
    "relwidth": 1 - __FUNCTION_FRAME_MARGIN_LEFT - __FUNCTION_FRAME_MARGIN_RIGHT
}


display_textbox_configprop = {}
display_textbox_placeprop = {}