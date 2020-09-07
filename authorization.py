'''окно авторизации пользователя'''
from tkinter import *
from tkinter import messagebox
from users_data_base import *

# Окно ввода логина пользователя
def auth():
    # кнопка ввести
    def click():
        if str(name_entry.get()):
            messagebox.showinfo("Добро пожаловать", "Добро пожаловать, " + name_entry.get())
            # поиск пользователя в базе
            auth_user(str(name_entry.get()))
        else:
            # если поле пользователя пустое
            messagebox.showerror("Ошибка ввода", "Вы не ввели имя пользователя")
            exit(0)

        root.destroy()

    # окно ввода логина
    root = Tk()
    root.title("Добро пожаловать в Морской бой")
    root.geometry("300x80+600+300")
    name = StringVar()
    name_label = Label(text="Введите имя пользователя:")
    name_label.grid(row=0, column=0, sticky="w")
    name_entry = Entry(textvariable=name)
    name_entry.focus_set()
    name_entry.grid(row=0, column=1, padx=5, pady=5)
    message_button = Button(text="Ввести", command=click)
    message_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")
    root.mainloop()
