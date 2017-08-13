import unittest

from ddt import ddt, data, unpack

from main import main

@ddt
class TestMain(unittest.TestCase):

    @data(
        ('dumbledore@hogwarts.com',     'No'),
        ('mcgonagall@hogwarts.owlery',  'No'),
        ('riddho@hogwarts.com',         'No'),
        ('wahed@hogwarts.com',          'Yes'),
        ('raida@Hogwarts.com',          'No'),
        ('riddho@hogwarts.com',         'No'),
        ('Raida@hogwarts.com',          'No'),
        ('raida@Hogwarts.com',          'No'),
        ('raida@hogWarts.com',          'No'),
        ('raida@hogwarts.Com',          'No')
    )
    @unpack
    def test_main_squares(self, email, result):
        self.assertEqual(
            main(email),
            result
        )
