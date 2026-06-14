from flask import Flask, request, jsonify, render_template
from models import db, Product, Order
from chatbot import process_message

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    print("User:", data["message"])

    reply = process_message(data["message"])

    print("Bot:", reply)

    return jsonify({
        "reply": reply
    })

with app.app_context():

    db.create_all()

    if Product.query.count() == 0:

        product1 = Product(
            name="iPhone 17",
            price=79999,
            stock=20,
            description="6.3-inch OLED, 128GB Storage"
        )

        product2 = Product(
            name="Samsung Galaxy S25",
            price=69999,
            stock=15,
            description="Snapdragon Processor, 256GB"
        )

        order1 = Order(
            id=1001,
            product_id=1,
            customer_name="Rahul",
            status="Processing"
        )

        order2 = Order(
            id=1002,
            product_id=2,
            customer_name="Anita",
            status="Shipped"
        )

        db.session.add(product1)
        db.session.add(product2)
        db.session.add(order1)
        db.session.add(order2)
        db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)