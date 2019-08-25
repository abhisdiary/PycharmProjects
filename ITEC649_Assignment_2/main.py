"""
Module to read data from CSV files and HTML file
to populate an SQL database

ITEC649 2019
"""

import csv
import sqlite3
from bs4 import BeautifulSoup
from database import DATABASE_NAME, create_tables


def read_relations(db, openfile):
    """Store the relations listed in filename into the database
    - db      : a connection to a database.
    - openfile: CSV file open for reading and holding a relation per line.
    This function does not return any values. After executing this function, each row of the CSV file
    will be stored as a relation in the database.

    Example of use:
    >>> db = sqlite3.connect(DATABASE_NAME)
    >>> with open('relations.csv') as f:
    >>>    read_relations(db, f)
    """
    cursor = db.cursor()
    relations_file = csv.reader(openfile, delimiter=",")
    next(relations_file, None)  # skip the header
    for row in relations_file:
        sql_insert_query = """INSERT INTO relations (product, location) VALUES (?,?)"""
        insert_tuple = (int(row[0]), int(row[1]))
        cursor.execute(sql_insert_query, insert_tuple)
    db.commit()


def read_locations(db, openfile):
    """Store the locations listed in the open file into the database
    - db      : a connection to a database.
    - openfile: CSV file open for reading and holding a location per line.
    This function does not return any values or print anything on screen. After executing this function,
    each row of the CSV file will be stored as a location in the database.

    Example of use:
    >>> db = sqlite3.connect(DATABASE_NAME)
    >>> with open('locations.csv') as f:
    >>>     read_locations(db, f)
    """

    cursor = db.cursor()
    locations_file = csv.reader(openfile, delimiter=",")
    next(locations_file, None)  # Skip the header
    for row in locations_file:
        sql_insert_query = """INSERT INTO `locations` (id, number, street, city, state) VALUES (?,?,?,?,?)"""
        insert_tuple = (int(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]))
        cursor.execute(sql_insert_query, insert_tuple)
    db.commit()


def read_stock(db, openfile):
    """Read the products from the open file and store them in the database
    - db      : a connection to a database.
    - openfile: HTML file open for reading and listing products.
    This function does not return any values or print anything on screen. After executing this function,
    the products found in the HTML file will be stored as product records in the database.

    Example of use:
    >>> db = sqlite3.connect(DATABASE_NAME)
    >>> with open('index.html') as f:
    >>>     read_stock(db, f)
    """
    cursor = db.cursor()
    html_doc = openfile.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    data = soup.find_all("div", class_='product')
    for e1 in data:
        product_id = e1.h2.a['href'].split('/')
        description = e1.h2.a.text
        cost = str(e1.find("div", class_='cost').text).replace("Â", "")
        stock = e1.find("div", class_='inventory').text
        stock = stock.split(' ')
        currency = cost[0]
        sql_insert_query = """ INSERT INTO `products` (`id`, `description`, `stock`, `price`, `currency`) VALUES (?,?,?,?,?)"""
        insert_tuple = (int(product_id[-1]), str(description), int(stock[0]), float(cost[1:]), str(currency))
        cursor.execute(sql_insert_query, insert_tuple)
    db.commit()


def report(db, openfile):
    """Generate a database report and store it in outfile
    - db      : a connection to a database
    - openfile: a CSV file open for writing
    This function does not return any values or print anything on screen. After executing this function,
    the file outfile will contain the product information, one row in the CSV file per product. Each row must
    contain the following information:
      - description
      - price (including the currency symbol)
      - amount in stock
      - store location

    Example of use:
    >>> db = sqlite3.connect(DATABASE_NAME)
    >>> with open('report.csv', 'w') as f:
    >>>     report(db, open('report.csv', 'w'))
    """
    headers = "description,price,currency,stock,location\n"
    openfile.write(headers)

    cursor_product_table = db.cursor()
    cursor_product_table.execute("""SELECT * FROM products ORDER BY price ASC""")
    for row in cursor_product_table:
        product_id = row[0]
        description = str(row[1])
        currency = row[4].replace("¬", "")
        price = str(row[3])
        amount_in_stock = str(row[2])

        cursor_relation_table = db.cursor()
        cursor_relation_table.execute("""SELECT location FROM relations WHERE product = ?""", (product_id,))
        location_id = cursor_relation_table.fetchone()[0]

        cursor_location_table = db.cursor()
        cursor_location_table.execute("""SELECT number, street, city, state FROM locations WHERE id = ?""",
                                      (location_id,))
        store_location = list_to_string(cursor_location_table.fetchone())
        csv_row = description + "," + price + "," + currency + "," + amount_in_stock + "," + store_location + "\n"
        openfile.write(csv_row)


def list_to_string(lst):
    """
    This function takes a list and returns a string where all the items of the list are concatenated together, separated by a comma & whitespace
    :param lst: List of integers or strings
    :return: string
    """
    s = [str(i) for i in lst]  # Converting integer list to string list
    string = str(", ".join(s))  # Joining list items
    string = '"' + string + '"'

    return string


def main():
    """Execute the main code that calls all functions
    This code should call the above functions to read the files "relations.csv",
    "locatons.csv" and "index.html", and generate "report.csv" as described in
    the assignment specifications.
    """
    db = sqlite3.connect('itec649.db')
    create_tables(db)

    # Write your code below
    db = sqlite3.connect('itec649.db')
    with open('index.html') as f:
        read_stock(db, f)

    with open('locations.csv') as locations:
        read_locations(db, locations)

    with open('relations.csv') as relations:
        read_relations(db, relations)

    with open('report.csv', 'w') as r:
        report(db, open('report.csv', 'w'))


# Do not edit the code below
if __name__ == '__main__':
    main()
