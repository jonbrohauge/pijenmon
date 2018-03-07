import unittest

try:
    from jenkinsapi.jenkins import Jenkins
except ImportError:
    print("Jenkins was not found")


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
