import sqlite3
import csv

db=sqlite3.connect("shop.db")
cursor = db.cursor()

cursor.execute("""
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    c.email,
    o.order_id,
    o.product_name,
    o.quantity,
    o.unit_price
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
WHERE c.status = 'active'
""")

data = cursor.fetchall()

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "customer_id",
        "name",
        "email",
        "order_id",
        "product_name",
        "quantity",
        "unit_price",
        "order_total"
    ])

    for row in data:
        customer_id, firstname, lastname, email, order_id, product, quantity, price = row
        name = firstname + " " + lastname
        total = quantity * price

        writer.writerow([
            customer_id,
            name,
            email,
            order_id,
            product,
            quantity,
            price,
            total
        ])

db.close()
print("csv written")
