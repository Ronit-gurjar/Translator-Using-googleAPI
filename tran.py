#imports
from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox

#app:-
root = Tk()
root.title("Language translator")
root.geometry("770x300")

#functions
def translate_it():
    pass

#Text boxes & buttons
original_text= Text(root, height=10, width=40)
original_text.grid(row=0, column=0, pady=20,padx=10)

translate_button= Button(root, text="Translate!", command=translate_it )
translate_button.grid(row=0, column=1, padx=10)

translated_text= Text(root, height=10, width=40)
translated_text.grid(row=0, column=2, pady=20,padx=10)

root.mainloop()