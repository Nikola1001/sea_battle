'''модуль отображения статистики(окно)'''
import tkinter as tk
import tkinter.ttk as ttk
import copy
from users_data_base import *


# класс окна с таблицей статистики
class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)
        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings
        # заголовки столбцов
        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER, width=60)
        # строки - статистика каждой клетки поля
        for row in rows:
            table.insert('', tk.END, values=tuple(row))
        # отображение кол-ва игр и побед пользователя
        table.insert('', tk.END, values=tuple(("Игр:", get_n_game())))
        table.insert('', tk.END, values=tuple(("Побед:", get_n_vin())))
        # ползунок прокрутки (вниз)
        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)


# метод вывода статистики в отдельном окне
def stat():
    print("получено для статистики ")
    print(stat_field)
    stat = copy.deepcopy(stat_field)
    for i in range(10):
        for j in range(10):
            if int(stat[i][j]) > 100:
                stat[i][j] = int(stat[i][j]) - 100
    row = []    # статистика построчно
    for i in range(10):
        row += stat[i * 10:(i * 10 + 10)]
    root = tk.Tk()
    # построение окна с таблицей
    table = Table(root, headings=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), rows=row)
    root.geometry("615x310")
    root.title('Statistics')
    table.pack(expand=tk.YES, fill=tk.BOTH)
    root.mainloop()
