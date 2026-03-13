import sqlite3

db = sqlite3.connect("shop.db")

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE,
    status TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_name TEXT,
    quantity INTEGER,
    unit_price FLOAT,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
)
""")

customers = [
    (1, "John", "Smith", "johnsmith@gmail.com", "active"),
    (2, "Joe", "Bloggs", "joebloggs@gmail.com", "active"),
    (3, "Emily", "Jones", "emilyjones@outlook.com", "suspended"),
    (4, "John", "Cena", "johncena@gmail.com", "active"),
    (5, "Noah", "Wilson", "noahwilson@gmail.com", "archived"),
]

orders = [
    (1, 1, "Pizza", 1, 15.00),
    (2, 1, "Chips", 2, 4.99),
    (3, 2, "Coke", 1, 2.00),
    (4, 3, "Burger", 2, 20.99),
    (5, 4, "Kebab", 3, 8.99),
]

cursor.executemany("""
INSERT OR IGNORE INTO customers
(customer_id, first_name, last_name, email, status)
VALUES (?, ?, ?, ?, ?)
""", customers)

cursor.executemany("""
INSERT OR IGNORE INTO orders
(order_id, customer_id, product_name, quantity, unit_price)
VALUES (?, ?, ?, ?, ?)
""", orders)

db.commit()
db.close()

print("Database setup.")