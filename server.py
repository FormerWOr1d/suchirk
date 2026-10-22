from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'sushirk_secret_2025_irnitu'  # Обязательно для сессий

# Список всех товаров (индекс = ID в корзине)
ITEMS = [
    ("Филадельфия", "OIP (1).webp", 1560),
    ("Калифорния", "OIP (2).webp", 1860),
    ("Темпура", "OIP (3).webp", 2300),
    ("Цезарь", "OIP (4).webp", 1890),
    ("Чигиряв", "OIP (5).webp", 2150),
    ("Эми", "OIP (6).webp", 2310),
    ("Дракон", "OIP (7).webp", 3100),
    ("Чамарев", "OIP (8).webp", 2110),
    ("ТОКИТОКИ", "OIP (9).webp", 2250),
    ("Дружка", "OIP.webp", 1490),
    ("ПиуПяу", "R (1).jpg", 2590),
    ("Япония", "R.jpg", 1910),
]

@app.route("/")
def index():
    return render_template("main.html", active="main")

@app.route("/catalog")
def catalog():
    return render_template("catalog.html", items=ITEMS, active="catalog")

@app.route("/add_to_cart/<int:item_id>")
def add_to_cart(item_id):
    if item_id < 0 or item_id >= len(ITEMS):
        return redirect(url_for('catalog'))
    
    if 'cart' not in session:
        session['cart'] = []
    
    session['cart'].append(item_id)
    session.modified = True
    return redirect(url_for('catalog'))

@app.route("/remove_from_cart/<int:index>")
def remove_from_cart(index):
    if 'cart' in session and 0 <= index < len(session['cart']):
        session['cart'].pop(index)
        session.modified = True
    return redirect(url_for('corzina'))

@app.route("/corzina")
def corzina():
    cart_items = []
    total = 0
    if 'cart' in session:
        for item_id in session['cart']:
            item = ITEMS[item_id]
            cart_items.append({
                'name': item[0],
                'img': item[1],
                'price': item[2]
            })
            total += item[2]
    
    return render_template("corzina.html", cart_items=cart_items, total=total, active="corzina")

@app.route("/support")
def support():
    return render_template("support.html", active="support")

@app.route("/author")
def author():
    return render_template("author.html", active="author")

if __name__ == "__main__":
    app.run(debug=True)