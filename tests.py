#-*-coding: utf-8 -*-

import unittest

import login


class LoginTest(unittest.TestCase):
    def test_database(self):
        result = login.test_database()
        self.assertIn("host", result)
        self.assertIn("database", result)
        self.assertIn("user", result)
        self.assertIn("password", result)
    
    def test_logging_in(self):
        result = login.test_logging_in()
        result_version = result.version()

        self.assertIn("server_version", result_version)
        self.assertIn("server_version_info", result_version)
        self.assertIsInstance(result_version["server_version_info"], list)
        self.assertIn("server_serie", result_version)
        self.assertIn("protocol_version", result_version)
    


if __name__ == "__main__":
    unittest.main()
        