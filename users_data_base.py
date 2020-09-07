'''модуль базы данных пользователи'''
import sqlite3

stat_field = [0] * 10
for i in range(10):
    stat_field[i] = [0] * 10
stat_field  # массив статистики каждой ячейки
n_name = ""  # имя пользователя
n_vin = 0  # кол-во побед
n_game = 0  # кол-во игр


# авторизация пользователя по логину
def auth_user(name):
    # подключение файла базы данных
    users = sqlite3.connect("users.db")
    with users:
        cur = users.cursor()
        # создание таблицы пользователей (если ее не было)
        cur.execute("CREATE TABLE IF NOT EXISTS Users(Name TEXT, Statis TEXT, Games INT, Victories INT)")
        # выбор строки с текущим пользователем
        cur.execute("SELECT * FROM Users WHERE Name = ?", [name])
        rows = cur.fetchall()
        global stat_field, n_game, n_vin, n_name
        n_name = name
        if rows == []:
            # если пользователь зашел в первый раз
            print("Пользователь зашел впервые.")
            stat_field_str = ""
            # переобразование статистики в строку
            for i in range(10):
                stat_field_str += ' '.join(str(x) for x in stat_field[i]) + ' '
            print(stat_field_str)
            print(stat_field)
            cur = users.cursor()
            # добавление значений в базу данных
            cur.execute("""INSERT INTO Users VALUES(?,?,?,?);""",
                        (str(name), str(stat_field_str), n_game, n_vin))
            cur.close()
        else:
            # если пользователь уже авторизован
            print((rows[0][0]) + " уже авторизован")
            stat_field_str = rows[0][1]  # статистика в виде строки
            print(stat_field_str)
            print(n_name)
            # преобразование сстатистики из строки в массив
            for i in range(10):
                stat_field[i] = stat_field_str.split(' ')[i * 10:(i * 10 + 10)]
            n_game = rows[0][2]  # кол-во игр
            n_vin = rows[0][3]  # кол-во побед
    cur.close()
    return rows


# сброс статистики
def clear_stat():
    # подключение файла с БД
    users = sqlite3.connect("users.db")
    with users:
        cur = users.cursor()
        # удаление таблицы пользователи
        cur.execute("DROP TABLE IF EXISTS Users")
    cur.close()
    print("Пользователь сбросил статистику")


# сохранение статистики в файл базы данных
def save_stat():
    # подключение файла с БД
    users = sqlite3.connect("users.db")
    global stat_field, n_game, n_vin
    # подсчет статистики по теории вероятности для каждой ячейки
    for i in range(10):
        for j in range(10):
            stat_field[i][j] = int(float(stat_field[i][j]) / n_game)
    # преобразование массива статистики в строчный формат
    stat_field_str = ""
    for i in range(10):
        stat_field_str += ' '.join(str(x) for x in stat_field[i]) + ' '
    print(stat_field)
    # обновление данных статистики в базе данных
    with users:
        cur = users.cursor()
        cur.execute("UPDATE Users SET Name=?, Statis =?, Games =?, Victories=? WHERE Name=?",
                    (n_name, stat_field_str, n_game, n_vin, n_name))
    cur.close()


# консольный вывод статистики
def print_stat():
    print('имя игрока' + n_name)
    print("кол-во побед " + str(n_vin))
    print("кол-во игр " + str(n_game))
    print(stat_field)


# инкремент кол-ва игр
def inc_n_game():
    global n_game
    n_game += 1


# инкремент кол-ва побед
def inc_n_vin():
    global n_vin
    n_vin += 1


# возвращает кол-во игр
def get_n_game():
    global n_game
    return n_game


# возвращает кол-во побед
def get_n_vin():
    global n_vin
    return n_vin
