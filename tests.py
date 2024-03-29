from check_pwd import check_pwd
import unittest


class TestCase(unittest.TestCase):
    def test1(self):
        pwd = ""
        self.assertFalse(check_pwd(pwd))

    def test2(self):
        pwd = "0"
        self.assertFalse(check_pwd(pwd))

    def test3(self):
        pwd = "111111111111111111111"
        self.assertFalse(check_pwd(pwd))

    def test4(self):
        pwd = "aaaaaaaaa"
        self.assertFalse(check_pwd(pwd))

    def test5(self):
        pwd = "AAAAAAAA0"
        self.assertFalse(check_pwd(pwd))

    def test6(self):
        pwd = "aaaaaaaa0"
        self.assertFalse(check_pwd(pwd))

    def test7(self):
        pwd = "AaAaAaAa0"
        self.assertFalse(check_pwd(pwd))

    def test8(self):
        pwd = "aA098!&%;"
        self.assertFalse(check_pwd(pwd))


if __name__ == '__main__':
    unittest.main()
