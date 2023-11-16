import tkinter as tk
import math
from tkinter import ttk

memory = 0
flag = False

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

def memory_store():
    global memory
    memory = float(entry.get())

def memory_recall():
    entry.delete(0, tk.END)
    entry.insert(0, str(memory))

def clear_memory():
    global memory
    memory = 0

def clear_all():
    entry.delete(0, tk.END)
    clear_memory()

def display_memory():
    entry.delete(0, tk.END)
    entry.insert(0, str(memory))

def button_click(number):
    global flag
    if flag:
        entry.delete(0, tk.END)
        flag = False
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear_entry():
    entry.delete(0, tk.END)

def clear_last_char():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    global flag
    expression = entry.get()
    try:
        expression = expression.replace('%', '/100').replace('×', '*').replace('÷', '/')
        result = eval(expression)
        result = round(result, 7)
        entry.delete(0, tk.END)
        entry.insert(0, result)
        history_list.insert(tk.END, f"{expression} = {result}")
        flag = True
    except SyntaxError:
        entry.delete(0, tk.END)
        entry.insert(0, "エラー")
        history_list.insert(tk.END, "計算エラー: 無効な式です")
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "エラー")
        history_list.insert(tk.END, "計算エラー: 0で割ることはできません")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, f"エラー: {e}")
        history_list.insert(tk.END, f"計算エラー: {e}")

def calculate_function(func):
    global flag
    expression = entry.get()
    try:
        value = float(expression)
        value_rad = math.radians(value)
        if func == 'sqrt':
            result = math.sqrt(value_rad)
        elif func == 'pow':
            result = math.pow(value, 2)
        else:
            result = getattr(math, func)(value_rad)
        result = round(result, 7)
        entry.delete(0, tk.END)
        entry.insert(0, result)
        if func == 'pow':
            history_list.insert(tk.END, f"{value}² = {result}")
        else:
            history_list.insert(tk.END, f"{func}({math.degrees(value_rad)}°) = {math.degrees(result)}°")
        flag = True
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "エラー: 無効な入力です")
        history_list.insert(tk.END, f"計算エラー: 無効な入力です")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, f"エラー: {e}")
        history_list.insert(tk.END, f"計算エラー: {e}")

def square_root():
    global flag
    current_value = float(entry.get())
    if current_value >= 0:
        result = math.sqrt(current_value)
        result = round(result, 7)
        entry.delete(0, tk.END)
        entry.insert(0, result)
        history_list.insert(tk.END, f"√({current_value}) = {result}")
        flag = True
    else:
        entry.delete(0, tk.END)
        entry.insert(0, "エラー")
        history_list.insert(tk.END, "計算エラー: 負の数の平方根は定義されていません")

def exit_app():
    root.quit()
    
def calculate_percentage():
    global flag
    expression = entry.get()
    try:
        result = eval(expression) / 100
        result = round(result, 7)
        entry.delete(0, tk.END)
        entry.insert(0, result)
        history_list.insert(tk.END, f"{expression}% = {result}")
        flag = True
    except (SyntaxError, ZeroDivisionError):
        entry.delete(0, tk.END)
        entry.insert(0, "エラー")
        history_list.insert(tk.END, "計算エラー: 無効な式です")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, f"エラー: {e}")
        history_list.insert(tk.END, f"計算エラー: {e}")


def convert_units(history_list):
    try:
        input_value = float(entry_value.get())
        input_unit = unit_var.get()

        result = 0

        if input_unit == "日から時間":
            result = input_value * 24 
            input_unit2 = "時間"
        elif input_unit == "時間から日":
            result = input_value / 24
            input_unit2 = "日"
        elif input_unit == "日から分":
            result = input_value * 24 * 60
            input_unit2 = "分"
        elif input_unit == "分から日":
            result = input_value / (24 * 60)
            input_unit2 = "日"
        elif input_unit == "日から秒":
            result = input_value * 24 * 60 * 60
            input_unit2 = "秒"
        elif input_unit == "秒から日":
            result = input_value / (24 * 60 * 60)
            input_unit2 = "日"
        elif input_unit == "時間から分":
            result = input_value * 60
            input_unit2 = "分"
        elif input_unit == "分から時間":
            result = input_value / 60
            input_unit2 = "時間"
        elif input_unit == "時間から秒":
            result = input_value * 60 * 60
            input_unit2 = "秒"
        elif input_unit == "秒から時間":
            result = input_value / (60 * 60)
            input_unit2 = "時間"
        elif input_unit == "分から秒":
            result = input_value * 60
            input_unit2 = "秒"
        elif input_unit == "秒から分":
            result = input_value / 60
            input_unit2 = "分"
        else:
            raise ValueError("無効な変換単位")

        result = round(result, 7)  # Round to 7 decimal places

        result_label.config(text=f"{input_value} {input_unit} = {result}{input_unit2}")
        history_list.insert(tk.END, f"{input_value} {input_unit} = {result}{input_unit2}")

    except ValueError:
        result_label.config(text="エラー: 数値を入力してください")
        history_list.insert(tk.END, "変換エラー: 数値を入力してください")
    except ZeroDivisionError:
        result_label.config(text="エラー: 0で割ることはできません")
        history_list.insert(tk.END, "変換エラー: 0で割ることはできません")
    except Exception as e:
        result_label.config(text=f"エラー: {e}")
        history_list.insert(tk.END, f"変換エラー: {e}")

def disable_entry(event):
    return "break"

root = tk.Tk()
root.title("アプリ")
root.minsize(250, 400)
root.maxsize(250, 400)

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

frame_calculator = tk.Frame(notebook)
notebook.add(frame_calculator, text="電卓")

frame_time_converter = tk.Frame(notebook)
notebook.add(frame_time_converter, text="時間変換")

frame_history = tk.Frame(notebook)
notebook.add(frame_history, text="履歴")

root.geometry("250x400")

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar)
menubar.add_cascade(label="ファイル", menu=file_menu)
file_menu.add_command(label="終了", command=exit_app)

entry = tk.Entry(frame_calculator, bg="white", font=('Helvetica', 20), justify="right", state='normal')
entry.pack(fill="x", padx=10, pady=10)

btn_width = 2
btn_height = 1

buttons = [
    ("7", "white"), ("8", "white"), ("9", "white"), ("%", "white"), ("√", "white"),
    ("4", "white"), ("5", "white"), ("6", "white"), ("÷", "white"), ("×", "white"),
    ("1", "white"), ("2", "white"), ("3", "white"), ("+", "white"), ("-", "white"),
    ("0", "white"), (".", "white"), ("=", "white"), ("←", "white"), ("AC", "white"),
]

button_frame = tk.Frame(frame_calculator)
button_frame.pack()

row_val = 1
col_val = 0

add_memory_button = tk.Button(button_frame, text="M+", command=add_to_memory, padx=5, pady=5, width=btn_width, height=btn_height, bg="white", font=('Helvetica', 14))
add_memory_button.grid(row=row_val, column=col_val, padx=2, pady=2)

col_val += 1

subtract_memory_button = tk.Button(button_frame, text="M-", command=subtract_from_memory, padx=5, pady=5, width=btn_width, height=btn_height, bg="white", font=('Helvetica', 14))
subtract_memory_button.grid(row=row_val, column=col_val, padx=2, pady=2)

col_val += 1

memory_recall_button = tk.Button(button_frame, text="MR", command=memory_recall, padx=5, pady=5, width=btn_width, height=btn_height, bg="white", font=('Helvetica', 14))
memory_recall_button.grid(row=row_val, column=col_val, padx=2, pady=2)

col_val += 1

clear_memory_button = tk.Button(button_frame, text="MC", command=clear_memory, padx=5, pady=5, width=btn_width, height=btn_height, bg="white", font=('Helvetica', 14))
clear_memory_button.grid(row=row_val, column=col_val, padx=2, pady=2)

col_val += 1

square_button = tk.Button(button_frame, text="x²", command=lambda: calculate_function('pow'), padx=5, pady=5, width=btn_width, height=btn_height, bg="white", font=('Helvetica', 14))
square_button.grid(row=row_val, column=col_val, padx=2, pady=2)

row_val += 1
col_val = 0

for label, color in buttons:
    if label == "←":
        tk.Button(button_frame, text=label, padx=5, pady=5, width=btn_width, height=btn_height, command=clear_last_char, bg=color, font=('Helvetica', 14)).grid(row=row_val, column=col_val, padx=2, pady=2)
    elif label == "AC":
        tk.Button(button_frame, text=label, padx=5, pady=5, width=btn_width, height=btn_height, command=clear_all, bg=color, font=('Helvetica', 14)).grid(row=row_val, column=col_val, padx=2, pady=2)
    elif label == "√":
        tk.Button(button_frame, text=label, padx=5, pady=5, width=btn_width, height=btn_height, command=square_root, bg=color, font=('Helvetica', 16)).grid(row=row_val, column=col_val, padx=2, pady=2)
    else:
        tk.Button(button_frame, text=label, padx=5, pady=5, width=btn_width, height=btn_height, command=lambda b=label: button_click(b) if b != "=" else calculate(), bg=color, font=('Helvetica', 16)).grid(row=row_val, column=col_val, padx=2, pady=2)
    
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

history_label = tk.Label(frame_history, text="履歴", bg="black", fg="white", font=('Helvetica', 16))
history_label.pack()

history_list = tk.Listbox(frame_history, bg="white", font=('Helvetica', 10))
history_list.pack(fill="both", expand=True)

instruction_label = tk.Label(frame_time_converter, font=('Helvetica', 14))
instruction_label.pack()

unit_var = tk.StringVar()
unit_var.set("時間から分")
unit_option_menu = tk.OptionMenu(frame_time_converter, unit_var, "日から時間", "時間から日", "日から分", "分から日", "日から秒", "秒から日", "時間から分", "分から時間", "時間から秒", "秒から時間", "分から秒", "秒から分")
unit_option_menu.pack()

entry_value = tk.Entry(frame_time_converter, font=('Helvetica', 14), justify="right")
entry_value.pack(fill="x", padx=10, pady=10)

convert_button = tk.Button(frame_time_converter, text="変換", command=lambda: convert_units(history_list), font=('Helvetica', 14))
convert_button.pack()

result_label = tk.Label(frame_time_converter, font=('Helvetica', 10))
result_label.pack()

entry.bind("<Key>", disable_entry)

root.mainloop()
