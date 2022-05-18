from unittest import TestCase
from unittest.mock import patch

from databases.core import Database
from wg_be_exam.actions.insertValue import InsertValue


class test_InsertValue(TestCase):

    async def test_insert_value(self):
        with patch.object(Database, 'execute', return_value=33) as mock_execute:
            await Database.execute()
            b = InsertValue.handle(1, 'a', Database)
            self.assertEqual(b.data_found, 33)
