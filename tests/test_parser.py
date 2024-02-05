import unittest
from iniutil.parser import cast_config_value, parse_ini


class ParserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_file_path = "resources/sample.ini"

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.test_file_path

    def test_ini_parser(self):
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
        self.assertEqual(expected, parse_ini(self.test_file_path))

    def test_value_cast(self):
        self.assertEqual(
            cast_config_value("https://api.example.com"), "https://api.example.com"
        )
        self.assertEqual(cast_config_value("3306"), 3306)
        self.assertEqual(cast_config_value("false"), False)
        self.assertEqual(cast_config_value("true"), True)
        self.assertEqual(cast_config_value("9.5"), 9.5)


if __name__ == "__main__":
    unittest.main()
