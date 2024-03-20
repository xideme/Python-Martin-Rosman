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
    """ Выполнение SQL запроса """
    try:
        cursor=connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Запрос выполнен успешно")
    except Error as e:
        print(f"Ошибка '{e}' при выполнении запроса")

def execute_read_query(connection,query:str):
    """ Выполнение SQL запроса и чтение результатов """
    cursor=connection.cursor()
    result=None
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        return result
    except Error as e:
        print(f"Ошибка '{e}'")

# Создание таблиц
create_categories_table="""
CREATE TABLE IF NOT EXISTS categories(
id_categories INTEGER PRIMARY KEY AUTOINCREMENT,
name_categories TEXT NOT NULL
);
"""
create_brands_table="""
CREATE TABLE IF NOT EXISTS brands(
id_brands INTEGER PRIMARY KEY AUTOINCREMENT,
name_brands TEXT NOT NULL
);
"""
create_products_table="""
CREATE TABLE IF NOT EXISTS products(
id_product INTEGER PRIMARY KEY AUTOINCREMENT,
product_name TEXT NOT NULL,
price REAL,
id_categories INTEGER,
id_brands INTEGER,
FOREIGN KEY(id_categories) REFERENCES categories(id_categories),
FOREIGN KEY(id_brands) REFERENCES brands(id_brands)
);
"""

# Заполнение таблиц данными
fill_categories="""
INSERT INTO categories (name_categories) VALUES ('Shoes'), ('Shirts'), ('Hoodie');
"""
fill_brands="""
INSERT INTO brands (name_brands) VALUES ('Vans'), ('Converse'), ('Adidas');
"""
fill_products="""
INSERT INTO products (product_name, price, id_categories, id_brands) VALUES 
('Converse ALL stars', 50.0, 1, 1), 
('Jeans', 20.0, 2, 2), 
('Adidas Shirt', 300.0, 3, 3);
"""

# Запросы к товарам
select_products_with_category_and_brand="""
SELECT products.product_name, products.price, categories.name_categories, brands.name_brands 
FROM products 
JOIN categories ON products.id_categories = categories.id_categories
JOIN brands ON products.id_brands = brands.id_brands;
"""

# Используем
conn=create_connection("C:/Users/soopk/source/repos/xideme/Python-Martin-Rosman/AppDataroivapood.db")

execute_query(conn, create_categories_table)
execute_query(conn, create_brands_table)
execute_query(conn, create_products_table)

execute_query(conn, fill_categories)
execute_query(conn, fill_brands)
execute_query(conn, fill_products)

products=execute_read_query(conn,select_products_with_category_and_brand)
print("Данные о товарах: ")
for product in products:
    print(product)