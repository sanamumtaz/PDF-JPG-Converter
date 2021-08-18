#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Aug 16, 2021 01:41:02 AM PKT  platform: Windows NT

import sys
import os
from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

import pdf2jpg_success

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
    from tkinter import filedialog

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


def select_file():
    curr_dir = os.getcwd()
    global file_path
    file_path = filedialog.askopenfilename(initialdir=curr_dir, title="Select PDF",
        filetypes=[("PDF File", "*.pdf")])

    if(file_path):
        global filename
        filename = file_path.split("/")[-1]
        w.Label3.configure(text=filename)


def convert2jpg():
    global filename
    output_folder_name = filename.split(".")[0]
    if not os.path.exists(output_folder_name):
        os.makedirs(output_folder_name)

    global file_path
    convert_from_path(
        file_path,
        output_folder=output_folder_name,
        output_file=output_folder_name,
        fmt="jpg",
        paths_only=True,
        poppler_path=r"./bin" if (sys.platform == "win32" or sys.platform == "cygwin") else NONE
    )
    destroy_window()
    pdf2jpg_success.vp_start_gui()
