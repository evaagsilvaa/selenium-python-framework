import time
from base.basepage import BasePage
import logging
import utilities.custom_logger as cl


class NavigationPage(BasePage):
    log = cl.customLogger(logging.DEBUG)  # passar Level

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _my_courses = "MY COURSES"
    _home = "HOME"
    _all_courses = "ALL COURSES"
    _support = "SUPPORT"
    _user_icon = "//button[@id='dropdownMenu1']"

    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses,locatorType="link")

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="link")

    def navigateToSupport(self):
        self.elementClick(locator=self._support, locatorType="link")

    def navigateToUserSettings(self):
        userSettingsElement = self.waitForElement(locator=self._user_icon, locatorType="xpath", pollFrequency=1)
        self.elementClick(element=userSettingsElement)


