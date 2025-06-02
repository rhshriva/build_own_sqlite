import unittest
from sqlengine.database import Database

class TestBasicDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database()

    def test_create_table(self):

        self.db.create_table('users', [('id', 'INTEGER'), ('name', 'TEXT')])
        self.assertEqual(len(self.db.tables), 1)
        self.assertEqual(self.db.tables['users'].columns, [('id', 'INTEGER'), ('name', 'TEXT')])
        self.assertEqual(len(self.db.tables['users'].rows), 0)

    def test_insert_and_select(self):

        self.db.create_table('users', [('id', 'INTEGER'), ('name', 'TEXT')])
        self.db.insert('users', [1, 'Alice'])
        self.db.insert('users', [2, 'Bob'])
        self.assertEqual(len(self.db.tables['users'].rows), 2)
        self.assertEqual(self.db.tables['users'].rows, [[1, 'Alice'], [2, 'Bob']])
        self.assertEqual(self.db.select('users'), [[1, 'Alice'], [2, 'Bob']])
        self.assertEqual(self.db.select('users', lambda row: row[1] == 'Alice'), [[1, 'Alice']])
        self.assertEqual(self.db.select('users', lambda row: row[1] == 'Charlie'), [])
        self.assertEqual(self.db.select('users', lambda row: row[0] == 1), [[1, 'Alice']])
        self.assertEqual(self.db.select('users', lambda row: row[0] == 3), [])
        self.assertEqual(self.db.select('users', lambda row: row[0] == 1 and row[1] == 'Alice'), [[1, 'Alice']])
        self.assertEqual(self.db.select('users', lambda row: row[0] == 1 and row[1] == 'Bob'), [])
        self.assertEqual(self.db.select('users', lambda row: row[0] == 2 and row[1] == 'Alice'), [])
        self.assertEqual(self.db.select('users', lambda row: row[0] == 2 and row[1] == 'Bob'), [[2, 'Bob']])
        self.assertEqual(self.db.select('users', lambda row: row[0] == 3 and row[1] == 'Alice'), [])

if __name__ == "__main__":
    # Discover all tests in the 'tests' directory
    loader = unittest.TestLoader()
    suite = loader.discover('tests')

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite) 