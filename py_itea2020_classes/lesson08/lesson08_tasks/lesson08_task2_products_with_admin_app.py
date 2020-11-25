from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


def get_query_result(sql_text):
    connect = sqlite3.connect('products.db')
    cursor = connect.cursor()
    cursor.execute(sql_text)
    result = cursor.fetchall()
    cursor.close()
    return result


def execute_sql(sql_text):
    connect = sqlite3.connect('products.db')
    cursor = connect.cursor()
    cursor.execute(sql_text)
    connect.commit()
    cursor.close()


@app.route('/')
def get_categories():
    categories = get_query_result('select id, category_name from category')
    return render_template('index.html', categories=categories)


@app.route('/<int:category_id>')
def get_products(category_id):
    category = get_query_result(f'select category_name from category where id = {category_id}')
    category_name = category[0][0]
    products = get_query_result(
        f'select id, product_name from product where category_id = {category_id} and is_available = 1')
    return render_template('products.html', category_id=category_id, category_name=category_name, products=products)


@app.route('/<int:category_id>/<int:product_id>')
def get_detailed_product(category_id, product_id):
    product = get_query_result(
        f'select product_name, price, amount from product where id = {product_id} and is_available = 1')
    product_name = product[0][0]
    price = product[0][1]
    amount = product[0][2]
    return render_template('product_details.html', product_name=product_name, price=price, amount=amount)


@app.route('/add_category', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        category_name = request.form['category_name']
        execute_sql(f'insert into category (category_name) values ("{category_name}")')
        return redirect('/')
    return render_template('add_category.html')


@app.route('/<int:category_id>/add_product', methods=['GET', 'POST'])
def add_product(category_id):
    if request.method == 'POST':
        product_name = request.form['product_name']
        amount = request.form['amount']
        price = request.form['price']
        is_available = int(request.form.get('is_available', 'off') == 'on')
        print(is_available)
        execute_sql(f'insert into product(product_name, category_id, price, amount, is_available) '\
                    f'values ("{product_name}", {category_id}, {price}, {amount}, {is_available})')
        return redirect('/' + str(category_id))
    return render_template('add_product.html', category_id=category_id)


app.run(debug=True)
