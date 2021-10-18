import sqlite3
from utils import *

con = sqlite3.connect('ecommerce.db')
cur = con.cursor()


def init_tables():
    tables = open('../tables.sql', 'r').read().split(';')[:-1]

    for table in tables:
        cur.execute(table + ";")

    con.commit()


def get_results_as_dict(query, arguments, extract_function):
    results = []
    for row in cur.execute(f"{query}", arguments):
        results.append(extract_function(row))

    return results


def get_customer_by_email(email):

    query = "SELECT * FROM Cliente WHERE email = ?"

    return get_results_as_dict(query, (email, ), extract_customer)


def get_customer_by_id(id):
    query = "SELECT * FROM Cliente WHERE id =?"

    return get_results_as_dict(query, (id, ), extract_customer)


def insert_customer(data):
    try:
        cur.execute(
            "INSERT INTO Cliente (nome, cognome, email, password_hash) VALUES (?, ?, ?, ?)", data)
        con.commit()
    except:
        print("insert error")


def get_categories():
    query = "SELECT * FROM Categoria"

    return get_results_as_dict(query, (), extract_category)


def insert_category(data):
    try:
        cur.execute(
            "INSERT INTO Categoria (nome) VALUES (?)", data)
        con.commit()
    except:
        print("insert error")


def get_order(customer_id):
    query = "SELECT * FROM Ordine WHERE id_cliente = ?"

    return get_results_as_dict(query, (customer_id, ), extract_order)


def insert_order(data):
    try:
        cur.execute(
            "INSERT INTO Ordine (id_cliente, data, totale, indirizzo_spedizione) VALUES (?, ?, ?, ?)", data)
        con.commit()
    except:
        print("insert error")


def get_report(order_id):
    query = "SELECT * FROM Segnalazione WHERE id_ordine = ?"

    return get_results_as_dict(query, (order_id, ), extract_report)


def get_report_by_customer(id_customer):
    query = "SELECT * FROM Segnalazione WHERE id_ordine = (SELECT * FROM Ordine WHERE id_cliente = ?)"

    return get_results_as_dict(query, (id_customer, ), extract_report)


def insert_report(data):
    try:
        cur.execute(
            "INSERT INTO Segnalazione (id_ordine, data_apertura, descrizione) VALUES (?, ?, ?)", data)
        con.commit()
    except:
        print("insert error")


def get_order_details(id_order):
    query = "SELECT * FROM ContenutoOrdine WHERE id_ordine=?"

    return get_results_as_dict(query, (id_order, ), extract_order_details)


def insert_order_details(data):
    try:
        cur.execute(
            "INSERT INTO ContenutoOrdine (id_ordine, id_prodotto, quantità) VALUES (?, ?, ?)", data)
        con.commit()
    except:
        print("insert error")


def get_all_products():
    query = "SELECT * FROM Prodotto"

    return get_results_as_dict(query, (), extract_product)


def get_product_by_category(category_name):
    query = "SELECT * FROM Prodotto WHERE id_categoria = (SELECT * FROM Categoria WHERE nome = ?)"

    return get_results_as_dict(query, (category_name, ), extract_product)


def insert_product(data):
    try:
        cur.execute(
            "INSERT INTO Prodotto (id_categoria, marca, modello, taglia, colore, prezzo, genere) VALUES (?, ?, ?, ?, ?, ?, ?)", data)
        con.commit()
    except:
        print("insert error")


def get_review_by_customer(id_customer):
    query = "SELECT * FROM Recensione WHERE id_cliente = ?"

    return get_results_as_dict(query, (id_customer, ), extract_review)


def get_review_by_product(id_product):
    query = "SELECT * FROM Recensione WHERE id_prodotto = ?"

    return get_results_as_dict(query, (id_product, ), extract_review)


def insert_review(data):
    try:
        cur.execute(
            "INSERT INTO Recensione (id_cliente, id_prodotto, data, rating, commento) VALUES (?, ?, ?, ?, ?)", data)
        con.commit()
    except:
        print("insert error")


def get_refund_by_customer(id_customer):
    query = "SELECT * FROM Rimborso WHERE id_cliente = ?"

    return get_results_as_dict(query, (id_customer, ), extract_refund)


def get_refund_by_employee(id_employee):
    query = "SELECT * FROM Rimborso WHERE id_dipendente = ?"

    return get_results_as_dict(query, (id_employee, ), extract_refund)


def insert_refund(data):
    try:
        cur.execute(
            "INSERT INTO Rimborso (id_cliente, id_dipendente, importo, data_versamento) VALUES (?, ?, ?, ?)", data)
        con.commit()
    except:
        print("insert error")


def get_closed_report_by_employee(id_employee):
    query = "SELECT * FROM SegnalazioneGestita WHERE id_dipendente = ?"

    return get_results_as_dict(query, (id_employee, ), extract_closed_report)


def get_closed_report_by_report(id_report):
    query = "SELECT * FROM SegnalazioneGestita WHERE id_segnalazione = ?"

    return get_results_as_dict(query, (id_report, ), extract_closed_report)


def insert_closed_report(data):
    try:
        cur.execute(
            "INSERT INTO SegnalazioneGestita (id_segnalazione, id_dipendente, descrizione, data) VALUES (?, ?, ?, ?)", data)
        con.commit()
    except:
        print("insert error")


def get_all_employee():
    query = "SELECT * FROM Dipendente"

    return get_results_as_dict(query, (), extract_employee)


def get_all_sales_between_date(date_start, date_end):
    query = "SELECT * FROM ProdottoScontato WHERE data_inizio >= ? AND data_fine <= ?"

    return get_results_as_dict(query, (date_start, date_end), extract_product_on_sale)


def insert_employee(data):
    try:
        cur.execute(
            "INSERT INTO Dipendente (data_assunzione, nome, cognome) VALUES (?, ?, ?)", data)
        con.commit()
    except:
        print("insert error")


def insert_sales(data):
    try:
        cur.execute(
            "INSERT INTO ProdottoScontato (id_prodotto, data_inizio, data_fine, prezzo_scontato) VALUES (?, ?, ?, ?)", data)
        con.commit()
    except:
        print("insert error")
