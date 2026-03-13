from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def dbconnect():
    db = sqlite3.connect("shop.db")
    db.row_factory = sqlite3.Row
    return db

@app.route("/customer/<int:customer_id>")
def getCustomer(customer_id):

    db = dbconnect()
    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM customers WHERE customer_id = ?",
        (customer_id,)
    )
   
    customer = cursor.fetchone()
    if customer is None:
        db.close()
        return {"error": "customer does not exist"}, 404
    
    cursor.execute(
        "SELECT * FROM orders WHERE customer_id = ?",
        (customer_id,)
    )
    orders = cursor.fetchall()
    db.close()

    return jsonify({
        "customer": dict(customer),
        "orders": [dict(order) for order in orders]
    })


if __name__ == "__main__":
    app.run(debug=True)