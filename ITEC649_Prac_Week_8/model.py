"""
Database models for week 5 workshop session

Tests are in test_model.py - run that file to test your code

"""

import sqlite3

DATABASE_NAME = "comp249.db"


def create_tables(db):
    """Create a database tables for the application given a database connection

    The database has a table named enrolments with the following fields:
        - name: a text field
        - unit: a text field that shows ONE of the units associated with the name

    """

    # code to create the database

    sql = """
DROP TABLE IF EXISTS enrolments;
CREATE TABLE enrolments (
    name text,
    unit text
);

"""
    db.executescript(sql)
    db.commit()


def add_enrollment(db, name, unit):
    """Add a single enrolment to the database

    name is a person (string)
    unit is a units name (string).

    adds a new record to the enrolments table with these two values
    """
    cur = db.cursor()
    cur.execute("INSERT INTO enrolments values (?,?)", (name, unit))
    db.commit()
    # code to add the data to the database


def list_enrolments(db):
    """Return a list of (person, unit) pairs ordered by person

    """
    # code to get the data from the database and return it
    cur = db.cursor()
    cur.execute("""SELECT * FROM enrolments ORDER BY name""")
    rows = cur.fetchall()
    return rows


if __name__ == "__main__":
    # run this module to create the database
    db = sqlite3.connect(DATABASE_NAME)
    create_tables(db)
