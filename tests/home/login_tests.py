from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com","abcabc")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1,"Title is incorrect")

        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin",result2, "Login failed")


    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logOut()
        self.lp.login("test1@email.com","abcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True
