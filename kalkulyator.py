import tkinter as tk
from tkinter import messagebox

# Функция для расчета среднего балла
def calculate_average():
    try:
        # Считывание значений из полей ввода
        grades = []
        for entry in entries:
            grade = float(entry.get())
            if 0 <= grade <= 10:  # Проверка на корректность оценки (от 0 до 10)
                grades.append(grade)
            else:
                raise ValueError("Оценки должны быть в пределах от 0 до 10.")
        
        # Расчет среднего балла
        if grades:
            average = sum(grades) / len(grades)
            result_label.config(text=f"Средний балл: {average:.2f}")
        else:
            messagebox.showwarning("Ошибка", "Пожалуйста, введите оценки.")
    
    except ValueError as ve:
        messagebox.showerror("Ошибка", f"Неверный ввод: {ve}")

# Список для хранения полей ввода оценок
entries = []

# Создание основного окна приложения
window = tk.Tk()
window.title("Калькулятор для среднего балла")

# Инструкция для пользователя
instruction_label = tk.Label(window, text="Введите оценки (по 10-бальной шкале):")
instruction_label.grid(row=10, column=0, columnspan=2, pady=10) 

# Поля ввода оценок
for i in range(1, 6):
    entry_label = tk.Label(window, text=f"Оценка {i}:")
    entry_label.grid(row=i, column=0)
    entry = tk.Entry(window)
    entry.grid(row=i, column=1)
    entries.append(entry)

window.geometry("1920x1080")
window.configure(bg="#808080")

# Кнопка для расчета
calculate_button = tk.Button(window, text="Рассчитать средний балл", command=calculate_average, bg="#f0f0f0")
calculate_button.grid(row=7, column=0, columnspan=2, padx=100*7, pady=1)

# Метка для отображения результата
result_label = tk.Label(window, text="Средний балл: ", font=("Arial", 14))
result_label.grid(row=0, column=0, columnspan=2, padx=10, pady=100)

# Запуск главного цикла приложения
window.mainloop()
