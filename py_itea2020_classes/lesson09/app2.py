from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
cars = [
    {'model': 'BMW',
     'price': 12000}
]

@app.route('/cars')
def get_cars():
    return render_template('get_cars.html', cars=cars)

@app.route('/add_cars', methods=['GET', 'POST'])
def add_cars():
    print(request.form)
    if request.method == 'POST':
        cars.append(request.form)
        print(cars)
        #return redirect('/cars')
        return redirect(url_for('get_cars'))
    return render_template('add_car.html', cars=cars)

app.run(debug=True)