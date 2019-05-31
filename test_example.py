#!/usr/bin/env python
""" various
"""

import unittest


class ThisTestCase(unittest.TestCase):
    """ A class for test cases for the functionality in ... """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_one_sample(self):
        self.assertTrue(True)
        self.assertFalse(True)

    def test_second_sample(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
