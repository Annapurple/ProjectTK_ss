import tkinter as tk
from tkinter import ttk, messagebox


def converting(num, base):
    if num == 0:
        return "0"
    digits = "0123456789ABCDEF"
    s = ""
    while num > 0:
        s = digits[num % base] + s
        num //= base
    return s


def correct_input(number_str, base):
    if not number_str:
        return False
    allowed = "0123456789ABCDEF"[:base]
    return all(char.upper() in allowed for char in number_str)


def convert():
    num_str = entry_num.get().strip().upper()
    base_from_str = entry_base_from.get().strip()
    base_to_str = entry_base_to.get().strip()
    if not num_str or not base_from_str or not base_to_str:
        messagebox.showwarning("Ошибка", "Заполни все три поля!")
        return
    try:
        base_from = int(base_from_str)
        base_to = int(base_to_str)
    except ValueError:
        messagebox.showerror("Ошибка", "Основание должно быть целым числом!")
        return
    if not (2 <= base_from <= 16) or not (2 <= base_to <= 16):
        messagebox.showerror("Ошибка", "Поддерживаются системы от 2 до 16!")
        return

    if not correct_input(num_str, base_from):
        messagebox.showerror(
            "Ошибка ввода",
            f"Цифры числа '{num_str}' недопустимы для {base_from}-й СС!"
        )
        return

    try:
        decimal_value = int(num_str, base_from)
        result = converting(decimal_value, base_to)
        label_result.config(text=result)
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))


root = tk.Tk()
root.title("Конвертер СС")
root.geometry("500x550")
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')

style = ttk.Style()
style.configure("TLabel", font=("Arial", 11))
style.configure("TButton", font=("Arial", 10, "bold"))
style.configure("Header.TLabel", font=("Arial", 11, "bold"))
style.configure("Result.TLabel", font=("Consolas", 16, "bold"), foreground="blue")

frame_systems = ttk.LabelFrame(root, text=" Системы счисления (2-16) ", padding=15)
frame_systems.pack(padx=15, pady=10, fill="x")

ttk.Label(frame_systems, text="Из какой СС:", style="Header.TLabel").grid(
    row=0, column=0, sticky="w", pady=5)
ttk.Label(frame_systems, text="В какую СС:", style="Header.TLabel").grid(
    row=1, column=0, sticky="w", pady=5)

entry_base_from = ttk.Entry(frame_systems, width=8, font=("Arial", 12))
entry_base_from.grid(row=0, column=1, padx=10, pady=5, sticky="w")
entry_base_from.insert(0, "10")

entry_base_to = ttk.Entry(frame_systems, width=8, font=("Arial", 12))
entry_base_to.grid(row=1, column=1, padx=10, pady=5, sticky="w")
entry_base_to.insert(0, "2")

frame_input = ttk.LabelFrame(root, text=" Ввод числа ", padding=15)
frame_input.pack(padx=15, pady=5, fill="x")

ttk.Label(frame_input, text="Число:").pack(side="left", padx=5)
entry_num = ttk.Entry(frame_input, font=("Arial", 12), width=22)
entry_num.pack(side="left", padx=10)

frame_result = ttk.LabelFrame(root, text=" Результат ", padding=15)
frame_result.pack(padx=15, pady=5, fill="x")

label_result = ttk.Label(frame_result, text="—", style="Result.TLabel")
label_result.pack()

frame_buttons = ttk.Frame(root)
frame_buttons.pack(pady=10)

btn_convert = ttk.Button(frame_buttons, text="Перевести",
                         command=convert, width=18)
btn_convert.pack()

ttk.Label(root, text="Поддерживаются системы от 2 до 16 (цифры 0-9 и буквы A-F)",
          foreground="gray", font=("Arial", 9)).pack(pady=5)

root.bind('<Return>', lambda event: convert())

root.mainloop()
