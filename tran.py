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
    #clear any previous translations
    translated_text.delete(1.0,END)
    try:
        #Get the languages from the Dictionary Keys
        #FROM language key
        for key,value in languages.items():
            if(value==original_combo.get()):
                from_language_key = key
        #TO language key
        for key,value in languages.items():
            if(value==translated_combo.get()):
                to_language_key = key
                
        #turn original text into a textblob       
        words = textblob.TextBlob(original_text.get(1.0,END))
        #translate text
        words = words.translate(from_lang=from_language_key, to=to_language_key)
        
        #output translated text to screen
        translated_text.insert(1.0,words)
        
    except Exception as e:
        messagebox.showerror("Translator",e)
def clear():
    original_text.delete(1.0,END)
    translated_text.delete(1.0,END)

#Grab language list from googletrans
languages= googletrans.LANGUAGES
language_list = list(languages.values())


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
translated_combo.grid(row=1, column=2)

#clear button
clear_button = Button(root, text="CLEAR", command=clear)
clear_button.grid(row=1,column=2)

root.mainloop()