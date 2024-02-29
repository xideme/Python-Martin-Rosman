from sqlite3 import connect, Error

def create_connection(path:str):
    """ Установка соединения с базой данных """
    connection=None
    try:
        connection=connect(path)
        print("Соединение успешно установлено")
    except Error as e:
        print(f"Произошла ошибка: '{e}'")
    return connection

def execute_query(connection, query:str):
    """ Создание таблицы """
    try:
        cursor=connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Таблица создана")
    except Error as e:
        print(f"Ошибка '{e}' при создании таблицы")

def execute_read_query(connection,query:str):
    """ Просмотр данных таблицы """
    cursor=connection.cursor()
    result=None
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        return result
    except Error as e:
        print(f"Ошибка '{e}'")
def execute_delete_query(connection,query:str):
    """Tabelist andmete eemaldamine"""
    try:
        cursor=connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabel-andmed on kustutatud")
    except Error as e:
        print(f"Viga '{e}'")


#-----------SQL ЗАПРОСЫ----------
create_users_table="""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
gender TEXT,
student BOOLEAN
);
"""
create_users="""
INSERT INTO
    users(name, age, gender, student)
VALUES
    ('Mati',45,'mees',0),
    ('Kadri',17,'naine',1),
    ('Andres',25,'mees',1),
    ('Mari',65,'naine',0),
    ('Anna',97,'naine',1);
"""
select_users="SELECT * FROM users"
delete_data_from_users="DELETE FROM users WHERE student=true"
delete_tabel_users="DROP TABLE"


#---------Используем-------

conn=create_connection("C:/Users/opilane/source/repos/xideme/Python-Martin-Rosman/AppData/data.db")

execute_query(conn, create_users_table)
execute_query(conn, create_users)
users=execute_read_query(conn,select_users)
print("Данные пользователей: ")
for user in users:
    print(user)

execute_delete_query(conn,delete_data_from_users)
users=execute_read_query(conn,select_users)
print("Kustutatud tudengid, on jäänud neid kellel student=0:")
for user in users:
    print(user)

print("Tabel on kustutanud")
for user in users:
    print(user)
execute_delete_query(conn,delete_tabel_users)
