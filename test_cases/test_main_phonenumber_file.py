import asyncio
import unittest
from phonenumber.main_phonenumber_file import get_ow_number


class TestStringMethods(unittest.TestCase):

    def Phoen_Check(self):
        self.assertEqual(asyncio.run(get_ow_number("https://www.wylieisd.net")), ['972.429.3000', '972.442.5368', '972.429.3000', '972.429.3000', '972.429.3000', '972.442.5368', '972.442.5368', '972.429.3009'])
        self.assertEqual("Dammala".upper(), "DAMMALA")


if __name__ == '__main__':
    unittest.main()
