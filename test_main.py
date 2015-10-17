import unittest

from main import f

class TestF(unittest.TestCase):

    def test_return(self):
        self.assertEqual(f(), 'qqq')


if __name__ == '__main__':
    unittest.main()