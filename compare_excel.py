import pandas as pd
import numpy as np
import os.path

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Excel Comparitor")
        self.minsize(640, 400)
        
        self.label = ttk.LabelFrame(self, text="Files to compare")
        self.label.pack()
        self.error = ttk.Label(self, text="")
        self.error.pack()
        self.files = []

        self.button()
        self.button2()
        
    def button2(self):    
        self.button2 = ttk.Button(self, text="Start Comparing", command= lambda: self.main())
        self.button2.pack(side = BOTTOM)

    def button(self):
        self.button = ttk.Button(self.label, text="Browse files", command= self.fileDialog)
        self.button.pack()
    
    def fileDialog(self):
        self.filenames = filedialog.askopenfilenames(initialdir=".", title="Select files to compare", filetype=(("excel", "*.xlsx"), ("All files", "*.*")))
        self.file_label = ttk.Label(self.label, text="")
        self.file_label.pack()
        self.file_label.configure(text = self.filenames)
        self.files = [x for x in self.filenames]
  
    def main(self):
        args = self.files
        self.files = []
        self.file_label.pack_forget()
        if not len(args) == 2:
            self.error.configure(text = "Incorrect number of files chosen (make sure its only 2). Try again.")
        else:
            df1 = pd.read_excel(args[0], na_values = ['NA'])
            df2 = pd.read_excel(args[1], na_values = ['NA'])
            df3 = df1.copy()
            if df1.equals(df2):
                comp = df1.values == df2.values
                rows, cols = np.where(comp == False)
                for item in zip(rows, cols):
                    df3.iloc[item[0], item[1]] = f"{df1.iloc[item[0], item[1]]} --> {df2.iloc[item[0], item[1]]}"
                file_loc = os.path.abspath("./diff.xlsx")
                df3.to_excel(file_loc, index=False, header=True)
                self.error.configure(text = f"File has been saved at {file_loc}")
            else:
                self.error.configure(text = "The structure of the files differs too much to be analyzed")




# This passes in the command line args to the program
if __name__ == "__main__":
    rt = Root()
    rt.mainloop()