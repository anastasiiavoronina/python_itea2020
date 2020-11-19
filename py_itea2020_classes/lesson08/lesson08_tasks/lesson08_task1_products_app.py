from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_query_result_from_products(sql_text):
    connect = sqlite3.connect('products.db')
    cursor = connect.cursor()
    cursor.execute(sql_text)
    result = cursor.fetchall()
    cursor.close()
    return result

@app.route('/')
def get_categories():
    categories = get_query_result_from_products('select id, category_name from category')
    return render_template('index.html', categories=categories)

@app.route('/<int:category_id>')
def get_products(category_id):
    category = get_query_result_from_products(f'select category_name from category where id = {category_id}')
    category_name = category[0][0]
    products = get_query_result_from_products(f'select id, product_name from product where category_id = {category_id} and is_available = 1')
    return render_template('products.html', category_id=category_id, category_name=category_name, products=products)

@app.route('/<int:category_id>/<int:product_id>')
def get_detailed_product(category_id, product_id):
    product = get_query_result_from_products(f'select product_name, price, amount from product where id = {product_id} and is_available = 1')
    product_name = product[0][0]
    price = product[0][1]
    amount = product[0][2]
    return render_template('product_details.html', product_name=product_name, price=price, amount=amount)


app.run(debug=True)
