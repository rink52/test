import tkinter as tk
from tkinter import ttk
import mysql.connector

# Функция для выполнения SQL-запроса
def execute_query():
    # Получаем введенный SQL-запрос из текстового поля
    query = query_entry.get()

    try:
        # Подключаемся к базе данных MySQL
        connection = mysql.connector.connect(
            host="ваш_хост",
            user="ваш_пользователь",
            password="ваш_пароль",
            database="ваша_база_данных"
        )

        # Создаем объект-курсор
        cursor = connection.cursor()

        # Выполняем SQL-запрос
        cursor.execute(query)

        # Получаем результат SQL-запроса
        result = cursor.fetchall()

        # Отображаем результат в текстовом поле
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, str(result))

        # Закрываем курсор и соединение с базой данных
        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Ошибка: {err}")

# Создаем главное окно
root = tk.Tk()
root.title("MySQL Query")

# Создаем метку и текстовое поле для ввода SQL-запроса
query_label = ttk.Label(root, text="Введите SQL-запрос:")
query_label.pack()

query_entry = ttk.Entry(root, width=40)
query_entry.pack()

# Создаем кнопку для выполнения SQL-запроса
execute_button = ttk.Button(root, text="Выполнить", command=execute_query)
execute_button.pack()

# Создаем текстовое поле для отображения результата
result_text = tk.Text(root, height=10, width=40)
result_text.pack()

# Запускаем главное окно
root.mainloop()