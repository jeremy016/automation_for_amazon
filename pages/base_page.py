import unittest
from seleniumbase import BaseCase
from selenium.webdriver.common.keys import Keys
from utils.locators import *
from utils.email_parser import EmailParser


# this Base class is serving basic attributes for every single page inherited from Page class

class BasePage(BaseCase):

    def setUp(self):
        super().setUp()
        # <<< Run custom code AFTER the super() line >>>
        self.main_page_locator = MainPageLocators
        self.login_page_locator = LoginPageLocators

    def tearDown(self):
        self.save_teardown_screenshot()
        if self.has_exception():
            # <<< Run custom code if the test failed. >>>
            pass
        else:
            # <<< Run custom code if the test passed. >>>
            pass
        # (Wrap unreliable code in a try/except block.)
        # <<< Run custom code BEFORE the super() line >>>
        super().tearDown()

    def get_locale(self):
        get_locale = self.get_locale_code()
        if 'en-US' == get_locale:
            get_locale = 'en-us'
        elif 'zh-TW' == get_locale:
            get_locale = 'en-tw'
            
        return get_locale

    def sendKeys(self, key=''):

        element = self.driver.find_element(self.login_page_locator.SUBMIT[1],self.login_page_locator.SUBMIT[0])
        if  key == 'ENTER':
            element.send_keys(Keys.ENTER)
        else:
            self._print("{} is invalid input.".format(key))

    def extract_otp(self):
        parser_worker = EmailParser()
        message = parser_worker.fetch_message()
        otp_text = parser_worker.extract_otp(message.html.body)

        return otp_text