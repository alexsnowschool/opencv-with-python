import unittest

import example


class ExampleTestSuite(unittest.TestCase):

    def test_run(self):
        self.assertEqual(example.run(), "running...")


if __name__ == '__main__':
    unittest.main()
