def extract_customer(data):
    return {
        'id': data[0],
        'name': data[1],
        'surname': data[2],
        'email': data[3]
    }


def extract_category(data):
    return {
        'id': data[0],
        'name': data[1],
        'total_articles': data[2]
    }


def extract_order(data):
    return {
        'id': data[0],
        'id_customer': data[1],
        'date': data[2],
        'total': data[3],
        'address': data[4],
        'pagato': data[5]
    }


def extract_report(data):
    return {
        'id_report': data[0],
        'date': data[1],
        'description': data[2]
    }


def extract_employee(data):
    return {
        'id': data[0],
        'hiring_date': data[1],
        'name': data[2],
        'surname': data[3],
        'tax_id': data[4],
        'handled_report': data[5]
    }


def extract_product(data):
    return {
        'id': data[0],
        'id_category': data[1],
        'brand': data[2],
        'model': data[3],
        'size': data[4],
        'color': data[5],
        'price': data[6],
        'rating': data[7],
        'gender': data[8]
    }


def extract_order_details(data):
    return {
        'id_order': data[0],
        'id_product': data[1],
        'quantity': data[2]
    }


def extract_review(data):
    return {
        'id_customer': data[0],
        'id_product': data[1],
        'date': data[2],
        'rating': data[3],
        'comment': data[4]
    }


def extract_refund(data):
    return {
        'id': data[0],
        'id_customer': data[1],
        'id_employee': data[2],
        'money': data[3],
        'date': data[4]
    }


def extract_closed_report(data):
    return {
        'id_report': data[0],
        'id_employee': data[1],
        'description': data[2],
        'date': data[3],
    }


def extract_product_on_sale(data):
    return {
        'id_product': data[0],
        'date_start': data[1],
        'date_end': data[2],
        'new_price': data[3],
    }
