import asyncio
import unittest
from phonenumber.main_phonenumber_file import get_number_list, get_ow_number, url_with_number

lst = ["Primary +49 8099887335", "Primary +49 8099887335", "Prary +49 8099887335", "Primary +49 8099887335",
       "Primary +49 8099887335"]


class TestValues(unittest.TestCase):

    def test_get_number_list(self):
        [self.assertEqual(asyncio.run(get_number_list(i)), "8099887335") for i in lst]

    def test_get_ow_number(self):
        self.assertEqual(asyncio.run(get_ow_number('http://norcroftapartments.com/')), [['(804) 232-5207', '(804) 232-4889']])
        self.assertEqual(asyncio.run(get_ow_number('http://norcroftapartments.com/')),
                         [['(804) 232-5207', '(804) 232-4889']])

    def test_url_with_number(self):
        self.assertEqual(url_with_number("http://norcroftapartments.com/"), ('"{\'http://norcroftapartments.com\': [\'(804) 232-5207\', \'(804) '
 "232-4889'], 'http://norcroftapartments.com/contact-us': ['(999) "
 '999-9999\']}"'))
