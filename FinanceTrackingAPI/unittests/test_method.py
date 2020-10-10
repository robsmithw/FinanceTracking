import unittest

class TestMethod(unittest.TestCase):

    def test_method(self):
        self.assertEqual(1, 1, "Should be 1")

if __name__ == '__main__':
    unittest.main()
    