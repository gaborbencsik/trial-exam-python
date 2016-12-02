import unittest
from e4 import greeter

class TestGreeter(unittest.TestCase):

    def test_real_name(self):
        self.assertEqual(greeter("Batman"), "Hello, Batman!")

    def test_no_name(self):
        self.assertEqual(greeter(""), "Hello, Mr Nobody!")

    def test_name_int(self):
        self.assertRaises(TypeError, greeter, 13)

if __name__ == '__main__':
    unittest.main()
