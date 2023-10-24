from flask import Flask, render_template, redirect, request
import dao

app = Flask(__name__)

@app.route('/')
def index():
    kw = request.args.get("kw")


    cates = dao.load_categories()
    products = dao.load_products(kw=kw)

    return render_template('index.html', categories=cates, products=products)

@app.route('/hello/<name>')
def hello_world(name):
    return "Hello %s" % name


@app.route('/details/<int:product_id>/<float:price>')
def product_price(product_id, price):
    return "San pham: %d: %.1f trieu VND" % (product_id, price)




if __name__ == '__main__':
    app.run(debug=True)