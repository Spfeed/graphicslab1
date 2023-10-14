import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

#бесполезный комментарий для коммита
if __name__ == '__main__':
    unittest.main()
