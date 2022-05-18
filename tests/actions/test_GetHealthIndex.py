import json
import requests_mock
from unittest import TestCase

from wg_be_exam.actions.getHealthIndex import GetHealthIndex
from wg_be_exam.config import Config


class test_GetHealthIndex(TestCase):
    def test_get_health_index(self):
        mocked_response = json.dumps({
            "facts": [{
                "Base year": "1996 = 100",
                "Health index": 1,
            }, {
                "Base year": "2004 = 100",
                "Health index": 2,
            }, {
                "Base year": "2013 = 100",
                "Health index": 3,
            }]
        })
        url = Config().URL_HEALT_INDEXES
        with requests_mock.Mocker() as mock:
            response = mock.get(url, text=mocked_response)

            index = GetHealthIndex.handle(url, 2004)

            self.assertEqual(2, index)

        self.assertEqual(1, mock.call_count)
