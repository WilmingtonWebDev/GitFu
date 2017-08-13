import unittest

from ddt import ddt, data, unpack

from main import main

@ddt
class TestMain(unittest.TestCase):

    @data(
        ([1],       [1]),
        ([2],       [4]),
        ([3],       [9]),
        ([1, 2, 3], [1, 4, 9]),
    )
    @unpack
    def test_main_squares(self, numbers, output):
        self.assertEqual(
            main(numbers),
            output
        )
