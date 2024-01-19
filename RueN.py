import tkinter as tk
from tkinter import scrolledtext

def convert_layout(text, from_layout, to_layout):
    layout_mapping = {
        'en': 'qwertyuiop[]asdfghjkl;\'zxcvbnm,./?&',
        'ru': 'йцукенгшщзхъфывапролджэячсмитьбю.,?&'
    }

    mapping_dict = dict(zip(layout_mapping[from_layout], layout_mapping[to_layout]))
    result = ''.join([mapping_dict.get(char, char) for char in text])
    return result

def convert_text():
    text_input = text_entry.get("1.0", "end-1c")
    converted_text = convert_layout(text_input, 'en', 'ru')
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, converted_text)
    result_text.config(state=tk.DISABLED)

def convert_text_back():
    text_input = text_entry.get("1.0", "end-1c")
    converted_text = convert_layout(text_input, 'ru', 'en')
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, converted_text)
    result_text.config(state=tk.DISABLED)

# Создаем главное окно
app = tk.Tk()
app.title("RueN, пойми друга долбоёба")

# Создаем элементы интерфейса
text_label = tk.Label(app, text="Текст тупого животного:")
text_entry = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=40, height=10)
convert_button = tk.Button(app, text="С обезьяньего на русский", command=convert_text)
convert_back_button = tk.Button(app, text="С русского на обезьянский", command=convert_text_back)
result_label = tk.Label(app, text="То, что он хотел написать:")
result_text = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=40, height=10, state=tk.DISABLED)

# Установка параметров resizable
app.resizable(width=False, height=False)

# Размещаем элементы интерфейса на форме
text_label.grid(row=0, column=0, pady=5)
text_entry.grid(row=1, column=0, pady=5)
convert_button.grid(row=2, column=0, pady=5)
convert_back_button.grid(row=3, column=0, pady=5)
result_label.grid(row=4, column=0, pady=5)
result_text.grid(row=5, column=0, pady=5)

# Запускаем главный цикл событий
app.mainloop()
