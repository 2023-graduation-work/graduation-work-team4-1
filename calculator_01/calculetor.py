import tkinter as tk
import math
from tkinter import ttk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
        history_list.insert(tk.END, f"{expression} = {result}")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "エラー")
        history_list.insert(tk.END, f"計算エラー: {e}")

def calculate_function(func):
    expression = entry.get()
    try:
        if func == 'sqrt':
            result = math.sqrt(eval(expression))
        else:
            result = getattr(math, func)(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(0, result)
        history_list.insert(tk.END, f"{func}({expression}) = {result}")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "エラー")
        history_list.insert(tk.END, f"計算エラー: {e}")

def exit_app():
    root.quit()

# 時間計算機能の関数
def convert_units(history_list):  # Pass history_list as a parameter
    input_value = float(entry_value.get())
    input_unit = unit_var.get()

    if input_unit == "時間から分":
        result = input_value * 60
        result_label.config(text=f"{input_value} 時間は {result} 分です")
    elif input_unit == "分から時間":
        result = input_value / 60
        result_label.config(text=f"{input_value} 分は {result} 時間です")
    elif input_unit == "時間から秒":
        result = input_value * 3600
        result_label.config(text=f"{input_value} 時間は {result} 秒です")
    elif input_unit == "秒から分":
        result = input_value / 60
        result_label.config(text=f"{input_value} 秒は {result} 分です")
    history_list.insert(tk.END, result_label.cget("text"))

root = tk.Tk()
root.title("アプリ")

# タブ用のNotebookウィジェット
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# タブ1: 電卓機能
frame_calculator = tk.Frame(notebook)
notebook.add(frame_calculator, text="電卓")

# タブ2: 時間計算機能
frame_time_converter = tk.Frame(notebook)
notebook.add(frame_time_converter, text="時間変換")

# Create a new tab for history
frame_history = tk.Frame(notebook)
notebook.add(frame_history, text="履歴")

# メインウィンドウの設定
root.geometry("200x450")  # Initial window size

# メニューバーを作成
menubar = tk.Menu(root)
root.config(menu=menubar)

# ファイルメニューを追加
file_menu = tk.Menu(menubar)
menubar.add_cascade(label="ファイル", menu=file_menu)
file_menu.add_command(label="終了", command=exit_app)

# 電卓機能

# 入力欄
entry = tk.Entry(frame_calculator, bg="white", font=('Helvetica', 20))
entry.pack(fill="x", padx=10, pady=10)

# Button width and height
btn_width = 2  # Reduce the button width
btn_height = 1  # Reduce the button height

# ボタン
buttons = [
    ("7", "white"), ("8", "white"), ("9", "white"), ("/", "white"),
    ("4", "white"), ("5", "white"), ("6", "white"), ("*", "white"),
    ("1", "white"), ("2", "white"), ("3", "white"), ("-", "white"),
    ("0", "white"), (".", "white"), ("=", "white"), ("+", "white"),
    ("sqrt", "white"), ("sin", "white"), ("cos", "white"), ("tan", "white"),
]

# Create button frame
button_frame = tk.Frame(frame_calculator)
button_frame.pack()

row_val = 0
col_val = 0
for label, color in buttons:
    if label in ["sqrt", "sin", "cos", "tan"]:
        tk.Button(button_frame, text=label, padx=5, pady=5, width=btn_width, height=btn_height, command=lambda b=label: calculate_function(b), bg=color, font=('Helvetica', 14)).grid(row=row_val, column=col_val, padx=2, pady=2)
    else:
        tk.Button(button_frame, text=label, padx=5, pady=5, width=btn_width, height=btn_height, command=lambda b=label: button_click(b) if b != "=" else calculate(), bg=color, font=('Helvetica', 16)).grid(row=row_val, column=col_val, padx=2, pady=2)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# クリアボタン
clear_button = tk.Button(frame_calculator, text="クリア", padx=5, pady=5, width=btn_width * 2, height=btn_height, command=clear, bg="white", font=('Helvetica', 16))
clear_button.pack()

# 履歴
history_label = tk.Label(frame_history, text="履歴", bg="black", fg="white", font=('Helvetica', 16))
history_label.pack()

history_list = tk.Listbox(frame_history, bg="white", font=('Helvetica', 14))
history_list.pack(fill="both", expand=True)

# 時間計算機能のウィジェット
instruction_label = tk.Label(frame_time_converter, text="変換したい単位を選択し、値を入力してください:", font=('Helvetica', 14))
instruction_label.pack()

unit_var = tk.StringVar()
unit_var.set("時間から分")
unit_option_menu = tk.OptionMenu(frame_time_converter, unit_var, "時間から分", "分から時間", "時間から秒", "秒から分")
unit_option_menu.pack()

entry_value = tk.Entry(frame_time_converter, font=('Helvetica', 16))
entry_value.pack(fill="x", padx=10, pady=10)

convert_button = tk.Button(frame_time_converter, text="変換", command=lambda: convert_units(history_list), font=('Helvetica', 14))
convert_button.pack()

result_label = tk.Label(frame_time_converter, font=('Helvetica', 14))
result_label.pack()

root.mainloop()
