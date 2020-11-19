from flask import Flask, render_template

app = Flask(__name__)

products = {'Onion': {'price': 12, 'in_stock': 1000, 'description': 'Лук'},
            'Tomato': {'price': 32, 'in_stock': 5000, 'description': 'Помидоры'},
            'Cucumber': {'price': 16, 'in_stock': 12000, 'description': 'Огурцы'}
            }

@app.route('/')
def hello_world():
    name = 'Nastya'
    return render_template('index.html', name=name)
    # html_text = """
    # <head>
    # <title>Hello World</title>
    # <body>
    #     <h1>Hello</h1>
    # </body>
    # </head>
    # """
    # return html_text
    # return 'Hello world'


@app.route('/goodbye')
def bye():
    return 'Bye'

@app.route('/products')
def get_products():
    return render_template('products.html', products=products)

@app.route('/products/<string:product_name>')
def get_detailed_product(product_name):
    return render_template('product_detail.html', product=products[product_name])
    #return str(products[product_name])


app.run(debug=True)
