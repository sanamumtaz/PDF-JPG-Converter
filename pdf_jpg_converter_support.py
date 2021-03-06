#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6

# package import
import sys

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

import os
import img2pdf
from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
# module import
import pdf_jpg_converter
import success

global conversion_mode
conversion_mode = "pdf"


def init(top, gui, mode, *args, **kwargs):
    global w, top_level, root, conversion_mode
    w = gui
    top_level = top
    root = top
    conversion_mode = mode

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


global name, filenames, file_paths
name = ""
filenames = []


def select_files():
    curr_dir = os.getcwd()
    global file_paths, conversion_mode
    if conversion_mode == "pdf":
        file_paths = [filedialog.askopenfilename(initialdir=curr_dir, title="Select PDF",
                                   filetypes=[("PDF File", "*.pdf")])]
    else:
        file_paths = filedialog.askopenfilenames(initialdir=curr_dir, title="Select JPG(s)",
            filetypes=[("JPG File", "*.jpeg *.jpg")])

    if len(file_paths):
        global filenames
        filenames = []
        for file_path in file_paths:
            file = file_path.split("/")[-1]
            filenames.append(file)
        w.Message1.configure(text=', '.join(filenames))
        global name
        if conversion_mode == "pdf":
            w.Button3["state"] = "normal"
        else:
            w.Button3["state"] = "normal" if len(name) else "disabled"


def is_name_empty(e):
    global name, filenames
    name = w.TEntry1.get()
    if len(name) and len(filenames):
        w.Button3["state"] = "normal"
    else:
        w.Button3["state"] = "disabled"


def convert_images():
    global name, file_paths
    with open(name+".pdf", "wb+") as f:
        f.write(img2pdf.convert(*file_paths))
    destroy_window()
    success.vp_start_gui("jpg")


def convert2jpg():
    global filenames
    output_folder_name = filenames[0].split(".")[0]
    if not os.path.exists(output_folder_name):
        os.makedirs(output_folder_name)

    global file_paths
    convert_from_path(
        file_paths[0],
        output_folder=output_folder_name,
        output_file=output_folder_name,
        fmt="jpg",
        paths_only=True,
        poppler_path=r"./bin" if (sys.platform == "win32" or sys.platform == "cygwin") else None
    )
    destroy_window()
    success.vp_start_gui("pdf")


def convert_pdf():
    destroy_window()
    pdf_jpg_converter.vp_start_gui("pdf")


def convert_jpg():
    destroy_window()
    pdf_jpg_converter.vp_start_gui("jpg")





