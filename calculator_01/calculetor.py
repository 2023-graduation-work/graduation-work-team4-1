import tkinter as tk
import math
from tkinter import ttk

memory = 0

def add_to_memory():
    global memory
    current_value = float(entry.get())
    memory += current_value
    entry.delete(0, tk.END)

def subtract_from_memory():
    global memory
    current_value = float(entry.get())
    memory -= current_value
    entry.delete(0, tk.END)

def display_memory():
    entry.delete(0, tk.END)
    entry.insert(0, str(memory))

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    global memory  # メモリーをクリア
    memory = 0
    entry.delete(0, tk.END)

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
        history_list.insert(tk.END, f"{expression} = {math.degrees(result)}°")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "エラー")
        history_list.insert(tk.END, f"計算エラー: {e}")

def calculate_function(func):
    expression = entry.get()
    try:
        value = float(expression)
        value_rad = math.radians(value)
        if func == 'sqrt':
            result = math.sqrt(value_rad)
        else:
            result = getattr(math, func)(value_rad)
        entry.delete(0, tk.END)
        entry.insert(0, result)
        history_list.insert(tk.END, f"{func}({math.degrees(value_rad)}°) = {math.degrees(result)}°")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "エラー")
        history_list.insert(tk.END, f"計算エラー: {e}")

def exit_app():
    root.quit()

def convert_units(history_list):
    input_value = float(entry_value.get())
    input_unit = unit_var.get()
    
    if input_unit == "日から時間":
        result = input_value * 24
        result_label.config(text=f"{input_value} 日は {result} 時間です")
    elif input_unit == "時間から日":
        result = input_value / 24
        result_label.config(text=f"{input_value} 時間は {result} 日です")
    elif input_unit == "日から分":
        result = input_value * 1440
        result_label.config(text=f"{input_value} 日は {result} 分です")
    elif input_unit == "分から日":
        result = input_value / 1440
        result_label.config(text=f"{input_value} 分は {result} 日です")
    elif input_unit == "日から秒":
        result = input_value * 86400
        result_label.config(text=f"{input_value} 日は {result} 秒です")
    elif input_unit == "秒から日":
        result = input_value / 86400
        result_label.config(text=f"{input_value} 秒は {result} 日です")
    elif input_unit == "時間から分":
        result = input_value * 60
        result_label.config(text=f"{input_value} 時間は {result} 分です")
    elif input_unit == "分から時間":
        result = input_value / 60
        result_label.config(text=f"{input_value} 分は {result} 時間です")
    elif input_unit == "時間から秒":
        result = input_value * 3600
        result_label.config(text=f"{input_value} 時間は {result} 秒です")
    elif input_unit == "秒から時間":
        result = input_value / 3600
        result_label.config(text=f"{input_value} 秒は {result} 時間です")
    elif input_unit == "分から秒":
        result = input_value * 60
        result_label.config(text=f"{input_value} 分は {result} 秒です")
    elif input_unit == "秒から分":
        result = input_value / 60
        result_label.config(text=f"{input_value} 秒は {result} 分です")
    history_list.insert(tk.END, result_label.cget("text"))


root = tk.Tk()
root.title("アプリ")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

frame_calculator = tk.Frame(notebook)
notebook.add(frame_calculator, text="電卓")

frame_time_converter = tk.Frame(notebook)
notebook.add(frame_time_converter, text="時間変換")

frame_history = tk.Frame(notebook)
notebook.add(frame_history, text="履歴")

root.geometry("200x450")

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar)
menubar.add_cascade(label="ファイル", menu=file_menu)
file_menu.add_command(label="終了", command=exit_app)

entry = tk.Entry(frame_calculator, bg="white", font=('Helvetica', 20))
entry.pack(fill="x", padx=10, pady=10)

btn_width = 2
btn_height = 1

buttons = [
    ("7", "white"), ("8", "white"), ("9", "white"), ("/", "white"),
    ("4", "white"), ("5", "white"), ("6", "white"), ("*", "white"),
    ("1", "white"), ("2", "white"), ("3", "white"), ("-", "white"),
    ("0", "white"), (".", "white"), ("=", "white"), ("+", "white"),
]

button_frame = tk.Frame(frame_calculator)
button_frame.pack()

row_val = 0
col_val = 0

add_memory_button = tk.Button(button_frame, text="M+", command=add_to_memory, padx=5, pady=5, width=btn_width, height=btn_height, bg="white", font=('Helvetica', 14))
add_memory_button.grid(row=row_val, column=col_val, padx=2, pady=2)

col_val += 1

subtract_memory_button = tk.Button(button_frame, text="M-", command=subtract_from_memory, padx=5, pady=5, width=btn_width, height=btn_height, bg="white", font=('Helvetica', 14))
subtract_memory_button.grid(row=row_val, column=col_val, padx=2, pady=2)

col_val += 1

display_memory_button = tk.Button(button_frame, text="M", command=display_memory, padx=5, pady=5, width=btn_width, height=btn_height, bg="white", font=('Helvetica', 14))
display_memory_button.grid(row=row_val, column=col_val, padx=2, pady=2)

col_val += 1

clear_button = tk.Button(button_frame, text="C", command=clear, padx=5, pady=5, width=btn_width, height=btn_height, bg="white", font=('Helvetica', 14))
clear_button.grid(row=row_val, column=col_val, padx=2, pady=2)

row_val += 1
col_val = 0

for label, color in buttons:
    if label in [""]:
        tk.Button(button_frame, text=label, padx=5, pady=5, width=btn_width, height=btn_height, command=lambda b=label: calculate_function(b), bg=color, font=('Helvetica', 14)).grid(row=row_val, column=col_val, padx=2, pady=2)
    else:
        tk.Button(button_frame, text=label, padx=5, pady=5, width=btn_width, height=btn_height, command=lambda b=label: button_click(b) if b != "=" else calculate(), bg=color, font=('Helvetica', 16)).grid(row=row_val, column=col_val, padx=2, pady=2)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

history_label = tk.Label(frame_history, text="履歴", bg="black", fg="white", font=('Helvetica', 16))
history_label.pack()

history_list = tk.Listbox(frame_history, bg="white", font=('Helvetica', 14))
history_list.pack(fill="both", expand=True)

instruction_label = tk.Label(frame_time_converter, font=('Helvetica', 14))
instruction_label.pack()

unit_var = tk.StringVar()
unit_var.set("時間から分")
unit_option_menu = tk.OptionMenu(frame_time_converter, unit_var,"日から時間", "時間から日", "日から分", "分から日", "日から秒", "秒から日", "時間から分", "分から時間", "時間から秒", "秒から時間", "分から秒", "秒から分")
unit_option_menu.pack()

entry_value = tk.Entry(frame_time_converter, font=('Helvetica', 16))
entry_value.pack(fill="x", padx=10, pady=10)

convert_button = tk.Button(frame_time_converter, text="変換", command=lambda: convert_units(history_list), font=('Helvetica', 14))
convert_button.pack()

result_label = tk.Label(frame_time_converter, font=('Helvetica', 10))
result_label.pack()

root.mainloop()