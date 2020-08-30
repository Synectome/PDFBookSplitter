from tkinter import *
from tkinter import filedialog
from pdf_parser import PDFP
import os


class App:
    def __init__(self, root):
        frame = Frame(root)
        frame.pack()
        self.file_select_window(frame, root)
        self.filename = ''
        self.original_file = ''

    def file_select_window(self, frame, root):
        leftframe = Frame(root, bd=2, bg="#38ba41")
        leftframe.pack(side=LEFT, padx=8)
        rightframe = Frame(root, bd=2, bg="#38ba41")
        rightframe.pack(side=RIGHT, padx=8)
        heading = Label(frame, text=" Welcome to the PDF Book Splitter ",
                             font=('calibri', 22, 'bold'),
                             background="#18d9ac",
                             foreground='black',
                             height=2)
        heading.pack(pady=4)

        labelFrame = LabelFrame(leftframe, text = "Open File")
        labelFrame.grid(column=0, row=1, padx=20, pady=20)

        select_file_button = Button(labelFrame, text="Browse A File", command=lambda: self.file_dialog(labelFrame))
        select_file_button.grid(column=1, row=1)

    def file_dialog(self, labelFrame):
        self.filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select A File")
        self.original_file = PDFP(self.filename)
        label = Label(labelFrame, text="")
        label.grid(column=1, row=2)
        label.configure(text=self.filename)

    def task_log_window(self):
        root = Tk()
        root.geometry("300x300")

        frame = Frame(root)
        frame.pack()

        my_entry = Entry(frame, width=20)
        my_entry.insert(0, 'Task Name')
        my_entry.pack(padx=5, pady=5)

        my_entry2 = Entry(frame, width=30)
        my_entry2.insert(0, 'Description')
        my_entry2.pack(padx=5, pady=5)

        button1 = Button(frame, text="Submit Log", width=8, bg="#18d9ac",
                         command=lambda: task_submition('log', root, my_entry, my_entry2))
        button1.pack(padx=3, pady=3)

        root.title("Log Entry Form")
        root.mainloop()