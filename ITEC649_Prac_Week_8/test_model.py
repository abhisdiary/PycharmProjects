"""
@author: Steve Cassidy

"""
import unittest
import sqlite3

from model import create_tables, add_enrollment, list_enrolments


class ModelTests(unittest.TestCase):

    def setUp(self):
        # open an in-memory database for testing
        self.db = sqlite3.connect(":memory:")

    def test_create_tables(self):
        """Test that create_tables makes the database tables"""

        create_tables(self.db)
        cur = self.db.cursor()

        # these queries return nothing but should succeed if the table is correct
        cur.execute("SELECT name, unit FROM enrolments")
        self.assertEqual([], cur.fetchall())

    def test_add_enrolment(self):
        """Test whether we can add data to the database"""
        create_tables(self.db)
        add_enrollment(self.db, 'Sue', 'COMP249')
        add_enrollment(self.db, 'Sue', 'COMP225')

        cur = self.db.cursor()
        cur.execute("SELECT name FROM enrolments WHERE unit='COMP249'")
        self.assertEqual([('Sue',)], cur.fetchall())

    def test_list_enrolments(self):
        """Test that we can list enrolments in the database"""

        create_tables(self.db)
        add_enrollment(self.db, 'Trevor', 'COMP225')
        add_enrollment(self.db, 'Sue', 'COMP249')

        en = list_enrolments(self.db)
        # should see the results in order
        self.assertListEqual([('Sue', 'COMP249'), ('Trevor', 'COMP225')], en)



if __name__ == "__main__":

    unittest.main()