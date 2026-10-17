from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "watchstore"

# ---------------- DATABASE ----------------
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nishi@2",
        database="watch_store"
    )


# ---------------- LOGIN PAGE ----------------
@app.route('/')
def login_page():
    return render_template('login.html')


# ---------------- LOGIN CHECK ----------------
@app.route('/login', methods=['POST'])
def user_login():

    db = get_db()
    cursor = db.cursor(dictionary=True)

    username = request.form['username']
    password = request.form['password']

    cursor.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s",
        (username, password)
    )

    user = cursor.fetchone()
    db.close()

    if user:
        session['user'] = username
        return redirect('/home')

    return "Invalid Username or Password"


# ---------------- HOME PAGE ----------------
@app.route('/home')
def home():

    db = get_db()
    cursor = db.cursor(dictionary=True)

    search = request.args.get('search')

    if search:
        cursor.execute(
            "SELECT * FROM products WHERE name LIKE %s",
            ('%' + search + '%',)
        )
    else:
        cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    db.close()

    return render_template("home.html", products=products)

@app.route('/search')
def search():

    keyword = request.args.get('search')

    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM products WHERE name LIKE %s",
        ('%' + keyword + '%',)
    )

    products = cursor.fetchall()

    db.close()

    return render_template("home.html", products=products)
# ---------------- ADD TO CART ----------------
@app.route('/add_cart/<int:id>')
def add_cart(id):

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO cart(product_id) VALUES(%s)",
        (id,)
    )

    db.commit()
    db.close()

    return redirect('/home')


# ---------------- CART PAGE ----------------
@app.route('/cart')
def cart():

    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT cart.id,
               products.name,
               products.price,
               products.image
        FROM cart
        JOIN products
        ON cart.product_id = products.id
    """)

    items = cursor.fetchall()
    db.close()

    total = sum(item['price'] for item in items)

    return render_template('cart.html', items=items, total=total)


# ---------------- REMOVE CART ITEM ----------------
@app.route('/remove/<int:id>')
def remove(id):

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM cart WHERE id=%s",
        (id,)
    )

    db.commit()
    db.close()

    return redirect('/cart')


# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)