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

"""Text boxes, Combo boxes & buttons"""
#Text box1
original_text= Text(root, height=10, width=40)
original_text.grid(row=0, column=0, pady=20,padx=10)

#button1
translate_button= Button(root, text="Translate!", command=translate_it )
translate_button.grid(row=0, column=1, padx=10)

#Text box2
translated_text= Text(root, height=10, width=40)
translated_text.grid(row=0, column=2, pady=20,padx=10)

#Combo box1
original_combo=ttk.Combobox(root, width=50, value=language_list)
original_combo.current(21)
original_combo.grid(row=1, column=0)

#Combo box2
translated_combo=ttk.Combobox(root, width=50, value=language_list)
translated_combo.current(21)
translated_combo.grid(row=1, column=0)

root.mainloop()