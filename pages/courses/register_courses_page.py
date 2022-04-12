from base.basepage import BasePage
import logging
import utilities.custom_logger as cl


class RegisterCoursesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_box = "//input[@id='search']"
    _search_button = "//button[@type='submit']"
    _course = "//h4[contains(text(),'{0}')]//parent::div//parent::a//parent::div//parent::div[@class='col-lg-4 col-md-4 col-sm-6 col-xs-12']"
    _enroll_button = "//button[contains(text(),'Enroll in')]"  # LINK_TEXT
    _scroll_in_to_element = "//div[@class='stripe-outer ']"
    _cc_num_iframe = "__privateStripeFrame3445"
    _cc_num = "//input[@name='cardnumber']"
    _cc_exp_iframe = "__privateStripeFrame8087"
    _cc_exp = "//input[@name='exp-date']"
    _cc_cvv_iframe = "__privateStripeFrame8086"
    _cc_cvv = "//input[@name='cvc']"
    _submit_enroll = "//button[@class='zen-subscribe sp-buy btn btn-default btn-lg btn-block btn-gtw btn-submit checkout-button dynamic-button']"
    _enroll_error_message_cc_num = "//span[contains(text(),'O número do seu cartão está incompleto.')]"
    _enroll_error_message_cc_exp = "//span[contains(text(),'A data de validade do seu cartão está incompleta.')]"
    _enroll_error_message_cc_cvv = "//span[contains(text(),'O código de segurança do seu cartão está incompleto.')]"


    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._search_box, locatorType="xpath")
        self.elementClick(locator=self._search_button, locatorType="xpath")


    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName),locatorType="xpath")

    def enrollInCourse(self):
        self.elementClick(locator=self._enroll_button,locatorType="xpath")

    def scrollDown(self):
        # Scroll Element Into View
        self.scrollIntoElement(locator=self._scroll_in_to_element,locatorType="xpath")

    def enterCardNum(self,num):
        #Enter Card Number
        self.switchFrameByIndex(self._cc_num)
        self.sendKeysWhenReady(num,locator=self._cc_num,locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        self.switchFrameByIndex(self._cc_exp)
        self.sendKeysWhenReady(exp,locator=self._cc_exp,locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        self.switchFrameByIndex(self._cc_cvv)
        self.sendKeysWhenReady(cvv, locator=self._cc_cvv, locatorType="xpath")
        self.switchToDefaultContent()

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll,locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self,	num="",	exp="",	cvv=""):
        self.enrollInCourse()
        self.scrollDown()
        self.enterCreditCardInformation(num,exp,cvv)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        result = self.isEnabled(locator=self._submit_enroll, locatorType="xpath", info="Enroll Button")
        return not result



