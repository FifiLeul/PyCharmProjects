import unittest

from ..task import lulu


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(lulu(1, 2), 2, msg="adds 1 + 2 to equal 3")

