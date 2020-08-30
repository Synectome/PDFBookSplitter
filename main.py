import os
from pdf_parser import PDFP
from tkinter import *
from GUI import App

if __name__=="__main__":
    # -- init init Stuff --
    cwd = os.getcwd()
    # -- GUI STUFF --
    root = Tk()
    root.geometry("600x800")
    app = App(root)
    root.title("PDF Book Splitter")
    root.mainloop()
    # ---------------

    # document = PDFP(cwd, 'Toshiro Kageyama - Lessons in the Fundamentals of Go.pdf')

    # page_num = 0
    # for page in document.pages:
    #     print(page_num)
    #     document.crop(page, page_num, split_point=0.6)
    #     page_num+=2
    #
    # document.make_pdf(1)
    # document.clean_up()
