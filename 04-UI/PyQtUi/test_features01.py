import unittest
import sys

from PyQt5.QtCore import QCoreApplication

from auth import Auth
import helper


class TestCase01(unittest.TestCase):
    def testConnect(self):
        q_app = QCoreApplication(sys.argv)
        self.assertTrue(helper.db_connect())

    def testMd5(self):
        self.assertEqual(helper.compute_hash("password"), "5f4dcc3b5aa765d61d8327deb882cf99")

    def testAuth(self):
        q_app = QCoreApplication(sys.argv)
        helper.db_connect()
        auth = Auth()
        self.assertEqual(auth.do_login("eko", "password"), True)


if __name__ == "__main__":
    unittest.main()
