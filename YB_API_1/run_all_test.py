# -*- coding:utf-8 -*-
import unittest
from HTMLTestRunner import HTMLTestRunner

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
