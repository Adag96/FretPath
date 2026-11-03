import unittest

import fretpath


class TestPackage(unittest.TestCase):
    def test_version(self):
        self.assertEqual(fretpath.__version__, "0.0.1")


if __name__ == "__main__":
    unittest.main()
