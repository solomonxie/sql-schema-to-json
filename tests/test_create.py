from unittest import TestCase

from sqlschematojson import parser
from sample import sql_statements


class TestCreate(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create(self):
        result = parser.parse_create(sql_statements.SQL_CREATE)
        self.assertEqual(type(result), dict)
        self.assertEqual(result['tablename'], 'some_table')
        self.assertEqual(result['primary_key'], 'tbid')
