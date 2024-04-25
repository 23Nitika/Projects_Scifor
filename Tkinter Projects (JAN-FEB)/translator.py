from googletrans import Translator, LANGUAGES
import tkinter as tk
from tkinter import ttk

def translate_text():
    translator = Translator()
    src_lang = source_language.get()
    dest_lang = destination_language.get()
    text_to_translate = entry_text.get("1.0",tk.END)
    translated_text = translator.translate(text_to_translate, src=src_lang, dest = dest_lang)
    output_text.delete("1.0",tk.END)
    output_text.insert("1.0",translated_text.text)


root = tk.Tk()
root.title("Tranlator")
root.configure(background='#1F2833')

source_label = ttk.Label(root, text="Source Language: ", background='#66FCF1')
source_label.grid(row=0, column=0, padx=5, pady=5)
source_language = ttk.Combobox(root, values=list(LANGUAGES.values()))
source_language.grid(row=0, column=1, padx=5, pady=5)
source_language.set('English')

destination_label = ttk.Label(root, text="Destination Language: ", background='#66FCF1')
destination_label.grid(row=1, column=0, padx=5, pady=5)
destination_language = ttk.Combobox(root, values=list(LANGUAGES.values()))
destination_language.grid(row=1, column=1, padx=5, pady=5)
destination_language.set('Select Language')

entry_label = ttk.Label(root, text="Enter text to translate: ", background='#66FCF1')
entry_label.grid(row=2,column=0,padx=5,pady=5)
entry_text = tk.Text(root, height=5, width=50, background='#45A29E', foreground='#0B0C10')
entry_text.grid(row=2, column=1, padx=5, pady=5)

translate_button = ttk.Button(root, text="Translate", command=translate_text, style='TButton')
translate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

output_label = ttk.Label(root, text="Translate text:", background='#66FCF1')
output_label.grid(row=4, column=0, padx=5, pady=5)
output_text = tk.Text(root, height = 5, width = 50, background='#45A29E', foreground='#0B0C10')
output_text.grid(row=4, column=1, padx=5, pady=5)

root.mainloop()