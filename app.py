from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

menu_items = [
    {"name": "Truffle Pasta", "price": "22", "description": "Fresh handmade tagliatelle.", "category": "mains"},
    {"name": "Burrata Salad", "price": "14", "description": "Heirloom tomatoes and basil.", "category": "starters"},
    
    # New: Pizza
    {"name": "Margherita Pizza", "price": "18", "description": "San Marzano tomatoes, fresh mozzarella, and basil.", "category": "pizza"},
    {"name": "Spicy Diavola", "price": "20", "description": "Salami, chili flakes, and hot honey drizzle.", "category": "pizza"},
    
    # New: Burritos
    {"name": "Carnitas Burrito", "price": "16", "description": "Slow-cooked pork, cilantro lime rice, and black beans.", "category": "mexican"},
    {"name": "Breakfast Burrito", "price": "13", "description": "Scrambled eggs, chorizo, potatoes, and house salsa.", "category": "mexican"},
    
    # New: Coffee
    {"name": "Oat Milk Latte", "price": "6", "description": "Double shot of espresso with creamy steamed oat milk.", "category": "coffee"},
    {"name": "Cold Brew", "price": "5", "description": "12-hour steep for a smooth, low-acid finish.", "category": "coffee"}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html", menu=menu_items)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':

    app.run(host='0.0.0.0',debug=True)
