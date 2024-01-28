import unittest
from parsini.parser import parse_ini


class Test(unittest.TestCase):
    def setUp(self):
        # Set up paths relative to the test script
        self.sample_ini_path = "resources/sample.ini"
        self.generic_ini_path = "resources/generic.ini"

    def test_example_case(self):
        """example case"""
        expected = {
            "owner": {
                "name": "John Doe",
                "organization": "Acme Widgets Inc.",
                "active": True,
                "rate": 2.03,
            },
            "database": {
                "server": "192.0.2.62",
                "port": 143,
                "file": '"payroll.dat"',
                "connection": "",
            },
        }
        actual = parse_ini(self.sample_ini_path)
        self.assertEqual(actual, expected)

    def test_generic_case(self):
        """generic case"""
        expected = {
            "section": {
                "b": False,
                "f": 206.201,
                "i": -55,
                "i1": 1,
                "b1": True,
                "b2": False,
                "s": "",
            },
        }
        actual = parse_ini(self.generic_ini_path)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()