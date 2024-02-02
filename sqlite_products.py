import sqlite3

connection = sqlite3.connect('products-sqlite.db')

cursor = connection.cursor()  # перемещение по записям в бд

cursor.execute("""CREATE TABLE IF NOT EXISTS Products
(products_id INTEGER PRIMARY KEY AUTOINCREMENT, product TEXT,
supplier TEXT, price_per_tonn INT)               
""")

productsToInsert = [
    ('Bananas', 'United Bananas', 7000),
    ('Avocados', 'United Avocados', 12000),
    ('Tomatos', 'United Tomatos', 3100)
]

# cursor.executemany("""
#         INSERT INTO Products(product, supplier, price_per_tonn)           
#         VALUES (?, ?, ?)                                            
#     """, productsToInsert)



cursor.execute("SELECT * FROM Products")
print(cursor.fetchall())

cursor.execute("SELECT supplier FROM Products")
print(cursor.fetchall())

price = (12000,)

cursor.execute("SELECT * FROM Products WHERE price_per_tonn=?", price)
print(cursor.fetchall())

new_price = (7000,)

cursor.execute("UPDATE Products SET supplier = 'United Doritos' WHERE price_per_tonn=?", new_price)
print(cursor.fetchall())

cursor.execute("SELECT supplier FROM Products")
print(cursor.fetchall())

cursor.execute("DELETE FROM Products WHERE products_id=3")

cursor.execute("SELECT * FROM Products")
print(cursor.fetchall())

cursor.execute("SELECT products_id FROM Products")
print(cursor.fetchall())

connection.commit()
connection.close()
