#imports
from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox

#app:-
root = Tk()
root.title("Language translator")
root.geometry("880x300")

#Text boxes
original_text= Text(root, height=10, width=40)
original_text.grid(row=0, column=0, pady=20,padx=10)

translated_text= Text(root, height=10, width=40)
translated_text.grid(row=0, column=2, pady=20,padx=10)

root.mainloop()