from unittest import TestCase
from unittest.mock import patch
import pandas

from wg_be_exam.actions.readZipcodesFile import ReadZipcodesFile

class test_ReadZipcodesFile(TestCase):
    def test_read_zipcodes_file(self):
        return_value = pandas.DataFrame({'zipcodes': ['1','1111 - 1111','3'], 'risk_factor': ['A', 'B', 'A']})
        return_value.set_index('zipcodes', inplace=True)
        with patch.object(pandas, 'read_csv', return_value=return_value) as mock_read_csv:
            output = ReadZipcodesFile.handle('fake.file')

            self.assertEqual(len(return_value.index.values), len(output.index.values))
