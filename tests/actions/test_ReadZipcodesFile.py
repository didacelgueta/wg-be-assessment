from unittest import TestCase
from unittest.mock import patch
import pandas

from wg_be_exam.actions.readZipcodesFile import ReadZipcodesFile

class test_ReadZipcodesFile(TestCase):
    def test_read_zipcodes_file(self):
        return_value = pandas.DataFrame({'zipcodes': [1,2,3], 'risk_factor': ['A', 'B', 'A']})
        with patch.object(pandas, 'read_csv', return_value=return_value) as mock_read_csv:
            output = ReadZipcodesFile.handle('fake.file')

            mocked_output = return_value.set_index('zipcodes')

            self.assertEqual(len(mocked_output.index.values), len(output.index.values))
