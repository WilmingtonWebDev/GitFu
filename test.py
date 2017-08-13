import unittest

from ddt import ddt, data, unpack

from main import main

@ddt
class TestMain(unittest.TestCase):

    @data(
        ('dumbledore@hogwarts.com',     'No'),
        ('mcgonagall@hogwarts.owlery',  'No'),
        ('riddho@hogwarts.com',         'No'),
        ('wahed@hogwarts.com',          'Yes')
    )
    @unpack
    def test_main_squares(self, email, result):
        self.assertEqual(
            main(email),
            result
        )
