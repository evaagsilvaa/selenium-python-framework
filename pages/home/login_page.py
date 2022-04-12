import time
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage
import logging
import utilities.custom_logger as cl


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)  # passar Level

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(self.driver)

    #Locators
    _login_link = "SIGN IN"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[@value='Login']"


    # Create methods
    def clickLoginLink(self):
        self.elementClick(self._login_link,locatorType="link")

    def enterEmail(self,email):
        self.sendKeys(email,self._email_field)

    def enterPassword(self,password):
        self.sendKeys(password,self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def getTitle(self):
        return self.driver.title



    def login(self, email="",password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        time.sleep(2)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//button[@id='dropdownMenu1']",locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[contains(text(),'Your username or password is invalid. Please try again.')]",locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("My Courses")

    def logOut(self):
        self.nav.navigateToUserSettings()
        logoutLinkElement = self.waitForElement(locator="//div[@class='navbar-buttons navbar-mob jqLoginLogout zl-navbar-rhs']//a[@href='/logout']",locatorType="xpath",pollFrequency=1)
        self.elementClick(element=logoutLinkElement)




