import asyncio
import unittest
from phonenumber.main_phonenumber_file import get_number_list


class Testvalues(unittest.TestCase):

    def test_joint(self):
        self.assertEqual(" ".join(["Python", "3.8"]), "Python 3.8")

    def test_join_with_comma(self):
        self.assertEqual(",".join(["Python", "3.8"]), "Python,3.8")

    def test_join_with_new_line_char(self):
        self.assertEqual("\n".join(["Python", "3.8"]), "Python\n3.8")

    def test_case_6(self):
        var2 = 4,
        self.assertTrue(isinstance(var2, tuple))
