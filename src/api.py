from flask import Flask, jsonify, request, Response
import hashlib
from database import database

app = Flask(__name__)


@app.route("/customers/email", methods=['GET'])
def get_customer_by_email():
    try:
        email = request.args.get('email')
        return jsonify(database.get_customer_by_email(email))
    except:
        return Response(status=500)


@app.route("/customers/<id>", methods=['GET'])
def get_customer_by_id(id):
    return jsonify(database.get_customer_by_id(id))


@app.route("/customers", methods=['GET', 'POST'])
def insert_customer():

    if request.method == 'POST':
        try:
            name = request.form['name']
            surname = request.form['surname']
            email = request.form['email']
            password_hash = hashlib.sha256(
                request.form['password'].encode('utf-8')).hexdigest()
            database.insert_customer((name, surname, email, password_hash))
            return Response(status=200)
        except:
            return Response(status=500)

    else:
        return jsonify(database.get_all_customers())


@app.route("/categories", methods=['GET', 'POST'])
def categories():
    if request.method == 'POST':
        try:
            name = request.form['name']
            database.insert_category((name,))
            return Response(status=200)
        except:
            return Response(status=500)

    else:
        return jsonify(database.get_categories())


@app.route("/employees", methods=['GET', 'POST'])
def employees():
    if request.method == 'POST':
        try:
            name = request.form['name']
            surname = request.form['surname']
            hiring_date = request.form['hiring_date']
            tax_id = request.form['tax_id']

            database.insert_employee((hiring_date, name, surname, tax_id))
            return Response(status=200)
        except:
            return Response(status=500)

    else:
        return jsonify(database.get_all_employee())


@app.route("/orders/<customer_id>", methods=['GET'])
def search_orders(customer_id):
    return jsonify(database.get_order(customer_id))


@app.route("/orders", methods=['GET', 'POST'])
def orders():
    if request.method == 'POST':
        try:
            id_customer = request.form['id_customer']
            address = request.form['address']

            database.insert_order((id_customer, address))
            return Response(status=200)
        except:
            return Response(status=500)

    else:
        return jsonify(database.get_all_orders())


@app.route("/pay/<order_id>", methods=['UPDATE'])
def pay(order_id):
    try:
        database.pay_order(order_id)
        return Response(status=200)
    except:
        return Response(status=500)


@app.route("/reports", methods=['GET', 'POST'])
def reports():
    if request.method == 'POST':
        try:
            id_order = request.form['id_order']
            description = request.form['description']

            database.insert_report((id_order, description))
            return Response(status=200)
        except:
            return Response(status=500)

    else:
        return jsonify(database.get_all_reports())


@app.route("/reports/order/<order_id>", methods=['GET'])
def search_report_by_order_id(order_id):
    return jsonify(database.get_report(order_id))


@app.route("/reports/customer/<customer_id>", methods=['GET'])
def search_report_by_customer_id(customer_id):
    return jsonify(database.get_report_by_customer(customer_id))


@app.route("/order/<id>/details", methods=['GET', 'POST'])
def order_details(id):
    if request.method == 'POST':
        try:
            id_order = id
            id_product = request.form['id_product']
            quantity = request.form['quantity']

            database.insert_order_details((id_order, id_product, quantity))
            return Response(status=200)
        except:
            return Response(status=500)

    else:
        return jsonify(database.get_order_details(id))


@app.route("/products", methods=['GET', 'POST'])
def products():
    if request.method == 'POST':
        try:
            id_category = request.form['id_category']
            brand = request.form['brand']
            model = request.form['model']
            size = request.form['size']
            color = request.form['color']
            price = request.form['price']
            gender = request.form['gender']

            database.insert_product(
                (id_category, brand, model, size, color, price, gender))
            return Response(status=200)
        except:
            return Response(status=500)

    else:
        return jsonify(database.get_all_products())


@app.route("/products/category", methods=['GET'])
def get_product_by_category():
    try:
        category = request.args.get('category')
        return jsonify(database.get_product_by_category(category))
    except:
        return Response(status=500)


@app.route("/reviews/customer/<id_customer>", methods=['GET'])
def get_reviews_by_customer(id_customer):
    return jsonify(database.get_review_by_customer(id_customer))


@app.route("/reviews/product/<id_product>", methods=['GET'])
def get_reviews_by_product(id_product):
    return jsonify(database.get_review_by_product(id_product))


@app.route("/reviews", methods=['GET', 'POST'])
def reviews():
    if request.method == 'POST':
        try:
            id_customer = request.form['id_customer']
            id_product = request.form['id_product']
            rating = request.form['rating']
            comment = request.form['comment']

            database.insert_review(
                (id_customer, id_product, rating, comment))
            return Response(status=200)
        except:
            return Response(status=500)

    else:
        return jsonify(database.get_all_reviews())


@app.route("/refunds/employee/<id>", methods=['GET'])
def refunds_by_employee(id):
    return jsonify(database.get_refund_by_employee(id))


@app.route("/refunds/customer/<id>", methods=['GET'])
def refunds_by_customer(id):
    return jsonify(database.get_refund_by_customer(id))


@app.route("/reports/closed", methods=['GET', 'POST'])
def closed_report():
    if request.method == 'POST':
        try:
            id_report = request.form['id_report']
            id_employee = request.form['id_employee']
            description = request.form['description']

            database.insert_closed_report(
                (id_report, id_employee, description))
            return Response(status=200)
        except:
            return Response(status=500)

    else:
        return jsonify(database.get_all_closed_report())


@app.route("/reports/closed/employee/<id>", methods=['GET'])
def closed_report_by_employee(id):
    return jsonify(database.get_closed_report_by_employee(id))


@app.route("/reports/closed/report/<id>", methods=['GET'])
def closed_report_by_report(id):
    return jsonify(database.get_closed_report_by_report(id))


@app.route("/sales/search", methods=['GET'])
def search_sales_by_date():
    try:
        date_start = request.args.get('date_start')
        date_end = request.args.get('date_end')
        return jsonify(database.get_all_sales_between_date(date_start, date_end))
    except:
        return Response(status=500)


@app.route("/sales/product/<id>", methods=['GET'])
def search_sales_by_product(id):
    return jsonify(database.get_sales_by_product(id))


@app.route("/sales", methods=['GET', 'POST'])
def sales():
    if request.method == 'POST':
        try:
            id_product = request.form['id_product']
            start_date = request.form['start_date']
            end_date = request.form['end_date']
            new_price = request.form['new_price']

            database.insert_sales(
                (id_product, start_date, end_date, new_price))
            return Response(status=200)
        except:
            return Response(status=500)

    else:
        return jsonify(database.get_all_sales())


database.init_tables()
