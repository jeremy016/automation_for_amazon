import time
import re
from utils.locators import *
from pages.base_page import BasePage
from utils.lang import login as LANG_OF_LOGIN
from utils import users
from utils import urls
from utils import regexs



class LoginPage(BasePage):
    
    def setUp(self):
        self.login_page_locator = LoginPageLocators
        super().setUp()

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

    def verify_elements_of_login_on_account_input_page(self, lang):
        self.wait_for_element_visible(*self.login_page_locator.EMAIL)
        # Elements on account page
        self.assert_element_present(*self.login_page_locator.ICON_LOGO)
        self.assert_element_present(*self.login_page_locator.LINK_LOGO)
        self.assert_element_present(*self.login_page_locator.TITLE_LOGIN)
        self.assert_element_present(*self.login_page_locator.LABEL_EMAIL)
        self.assert_element_present(*self.login_page_locator.LEGAL_TEXT)
        self.assert_element_present(*self.login_page_locator.CONDITIONS_OF_USE)
        self.assert_element_present(*self.login_page_locator.PRIVACY_NOTICE)
        self.assert_element_present(*self.login_page_locator.NEED_HELP)
        self.assert_element_present(*self.login_page_locator.OTHER_ISSUES)
        self.assert_element_present(*self.login_page_locator.NEW_TO_AMAZON)
        self.assert_element_present(*self.login_page_locator.SUBMIT_CREATE_ACCOUNT)
        self.assert_element_present(*self.login_page_locator.EMAIL)
        self.assert_element_present(*self.login_page_locator.CONTINUE)        
        # Text on account page
        self.assert_text(LANG_OF_LOGIN.LOGIN[lang]['title_signin'] ,*self.login_page_locator.TITLE_LOGIN)
        self.assert_text(LANG_OF_LOGIN.LOGIN[lang]['label_account'] ,*self.login_page_locator.LABEL_EMAIL)
        self.assert_text(LANG_OF_LOGIN.LOGIN[lang]['submit_continue'] ,*self.login_page_locator.CONTINUE)
        self.assert_text(LANG_OF_LOGIN.LOGIN[lang]['legal_text'] ,*self.login_page_locator.LEGAL_TEXT)
        self.assert_text(LANG_OF_LOGIN.LOGIN[lang]['text_need_help'] ,*self.login_page_locator.NEED_HELP)
        super().find_element(*self.login_page_locator.NEED_HELP).click()
        self.assert_text(LANG_OF_LOGIN.LOGIN[lang]['text_forgot_password'] ,*self.login_page_locator.FORGOT_PASSWORD)
        self.assert_text(LANG_OF_LOGIN.LOGIN[lang]['text_other_issues'] ,*self.login_page_locator.OTHER_ISSUES)
        self.assert_text(LANG_OF_LOGIN.LOGIN[lang]['text_new_to_amazon'] ,*self.login_page_locator.NEW_TO_AMAZON)
        text_create_account_submit = self.get_text(*self.login_page_locator.SUBMIT_CREATE_ACCOUNT)
        self.assert_true(LANG_OF_LOGIN.LOGIN[lang]['submit_create_your_Amazon_account'] in text_create_account_submit , msg='submit_create_your_Amazon_account wrong. "{0}"!="{1}"'.format(LANG_OF_LOGIN.LOGIN[lang]['submit_create_your_Amazon_account'],text_create_account_submit))
        # Links
        link_of_conditions_of_use = self.get_attribute(self.login_page_locator.CONDITIONS_OF_USE[0],'href')
        link_of_privice_notice = self.get_attribute(self.login_page_locator.PRIVACY_NOTICE[0],'href')
        regexp_of_conditions_of_use = re.compile(regexs.REGEXP_OF_CONDITIONS_OF_USE)
        self.assert_true(regexp_of_conditions_of_use.search(link_of_conditions_of_use), "Not match, Got:{}".format(link_of_conditions_of_use))
        regexp_of_privice_notice = re.compile(regexs.REGEXP_OF_PRIVICE_NOTICE)
        self.assert_true(regexp_of_privice_notice.search(link_of_privice_notice), "Not match, Got:{}".format(link_of_privice_notice))

    def verify_elements_of_login_on_password_input_page(self, lang):
        self.wait_for_element_visible(*self.login_page_locator.PASSWORD)
        # Elements on account page
        self.assert_element_present(*self.login_page_locator.ICON_LOGO)
        self.assert_element_present(*self.login_page_locator.LINK_LOGO)
        self.assert_element_present(*self.login_page_locator.TITLE_LOGIN)
        self.assert_element_present(*self.login_page_locator.LABEL_PASSWORD)
        self.assert_element_present(*self.login_page_locator.EMAIL_TEXT)
        self.assert_element_present(*self.login_page_locator.CHANGE_LOGIN)
        self.assert_element_present(*self.login_page_locator.PASSWORD)
        self.assert_element_present(*self.login_page_locator.SUBMIT)
        self.assert_element_present(*self.login_page_locator.FORGOT_PASSWORD)
        self.assert_element_present(*self.login_page_locator.KEEP_SIGNED_IN_CHECKBOX)
        self.assert_element_present(*self.login_page_locator.KEEP_SIGNED_IN_LABEL)
        self.assert_element_present(*self.login_page_locator.KEEP_SIGNED_IN_DETAIL)
        # Text on account page
        self.assert_text(LANG_OF_LOGIN.LOGIN[lang]['change'] ,*self.login_page_locator.CHANGE_LOGIN)
        self.assert_text(LANG_OF_LOGIN.LOGIN[lang]['label_password'] ,*self.login_page_locator.LABEL_PASSWORD)
        self.assert_text(LANG_OF_LOGIN.LOGIN[lang]['forgot_your_password'] ,*self.login_page_locator.FORGOT_PASSWORD)
        self.assert_text(LANG_OF_LOGIN.LOGIN[lang]['sign_in'] ,*self.login_page_locator.TEXT_SUBMIT)
        self.assert_text(LANG_OF_LOGIN.LOGIN[lang]['keep_me_signed_in'] ,*self.login_page_locator.KEEP_SIGNED_IN_LABEL)
        self.assert_text(LANG_OF_LOGIN.LOGIN[lang]['Details'] ,*self.login_page_locator.KEEP_SIGNED_IN_DETAIL)
        # self._print(self.get_text(*self.login_page_locator.KEEP_SIGNED_IN_DETAIL))

    def verify_error_message_without_account(self, lang):
        self.assert_text(LANG_OF_LOGIN.LOGIN[lang]['warning_of_no_account'] ,*self.login_page_locator.EMAIL_CONTENT_ALERT)

    def verify_error_message_without_password(self, lang):
        self.assert_text(LANG_OF_LOGIN.LOGIN[lang]['warning_of_no_password'] ,*self.login_page_locator.PASSWORD_CONTENT_ALERT)

    def verify_auth_error_mssage_when_submit_with(self, lang, situation=''):
        # Temp condition
        if self.is_element_visible(*self.login_page_locator.AUTH_CAPTCHA_IMAGE):
            self.fail(msg="The graphic recognition module has not been developed yet.")

        self.wait_for_element_visible(*self.login_page_locator.AUTH_ERROR_MESSAGE_BOX)
        # Elements on account page
        self.assert_element_present(*self.login_page_locator.AUTH_ERROR_MESSAGE_ICON)
        self.assert_element_present(*self.login_page_locator.AUTH_ERROR_MESSAGE_HEADER)
        self.assert_element_present(*self.login_page_locator.AUTH_ERROR_MESSAGE_CONTENT)
        # Text on account page
        self.assert_text(LANG_OF_LOGIN.LOGIN[lang]['auth_alert_header'] ,*self.login_page_locator.AUTH_ERROR_MESSAGE_HEADER)

        if situation == "invalid_email_format":
            self.assert_text(LANG_OF_LOGIN.LOGIN[lang]['auth_alert_content_with_email_not_found'] ,*self.login_page_locator.AUTH_ERROR_MESSAGE_CONTENT)
        elif situation == 'invalid_phone_format':
            self.assert_text(LANG_OF_LOGIN.LOGIN[lang]['auth_alert_content_with_email_not_found'] ,*self.login_page_locator.AUTH_ERROR_MESSAGE_CONTENT)
        elif situation == "wrong_password":
            self.assert_text(LANG_OF_LOGIN.LOGIN[lang]['auth_alert_content_with_wrong_password'] ,*self.login_page_locator.AUTH_ERROR_MESSAGE_CONTENT)
        else:
            self.assert_true(False,"Not this situation('{}')".format(situation))

    def verify_auth_error_mssage_when_submit_with_invalid_password(self, lang):
        self.wait_for_element_visible(*self.login_page_locator.AUTH_ERROR_MESSAGE_BOX)
        # Elements on account page
        self.assert_element_present(*self.login_page_locator.AUTH_ERROR_MESSAGE_ICON)
        self.assert_element_present(*self.login_page_locator.AUTH_ERROR_MESSAGE_HEADER)
        self.assert_element_present(*self.login_page_locator.AUTH_ERROR_MESSAGE_CONTENT)
        # Text on account page
        self.assert_text(LANG_OF_LOGIN.LOGIN[lang]['auth_alert_header'] ,*self.login_page_locator.AUTH_ERROR_MESSAGE_HEADER)
        self.assert_text(LANG_OF_LOGIN.LOGIN[lang]['auth_alert_content'] ,*self.login_page_locator.AUTH_ERROR_MESSAGE_CONTENT)

    def verify_password_is_in_masked(self):
        # check inuput type
        input_type = self.get_attribute(self.login_page_locator.PASSWORD[0],'type',self.login_page_locator.PASSWORD[1])
        self._print("Input_type:{}".format(input_type))
        self.assert_equal('password',input_type,"Verify that the password type is worng, Got:{}".format(input_type))
        
    def enter_email(self, email):
        self.find_element(*self.login_page_locator.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.find_element(*self.login_page_locator.PASSWORD).send_keys(password)

    def enter_create_password(self, password):
        self.find_element(*self.login_page_locator.AP_FPP_PASSWORD).send_keys(password)

    def enter_create_password_check(self, password):
        self.find_element(*self.login_page_locator.AP_FPP_PASSWORD_CHECK).send_keys(password)

    def enter_otp(self, otp):
        self.find_element(*self.login_page_locator.EMAIL_CVF).send_keys(otp)

    def click_continue_button(self):
        super().find_element(*self.login_page_locator.CONTINUE).click()

    def click_continue_button_on_authentication_required(self):
        super().find_element(*self.login_page_locator.CONTINUE_AUTHENTICATION_REQUIRED).click()

    def click_login_button(self):
        super().find_element(*self.login_page_locator.SUBMIT).click()

    def click_forgot_password_button(self):
        super().find_element(*self.login_page_locator.FORGOT_PASSWORD).click()

    def select_remember_me(self):
        self.select_if_unselected(*self.login_page_locator.KEEP_SIGNED_IN_CHECKBOX)

    def insert_password(self,user):
        user = users.get_user(user)
        self.enter_password(user["password"])

    def insert_otp(self):
        otp_text = self.extract_otp()
        self.enter_otp(otp_text)
        self.click_continue_button_on_authentication_required() 

    def insert_two_password_check(self,user):
        user = users.get_user(user)
        self.enter_create_password(user["password"])
        self.enter_create_password_check(user["password"])
        self.click_continue_button()

    def insert_account_if_no_value(self, user):
        user = users.get_user(user)
        value_of_mail = self.get_attribute(self.login_page_locator.EMAIL[0],'value',self.login_page_locator.EMAIL[1])
        if not value_of_mail:
            self.enter_email(user["email"])
        self.click_continue_button()

    def login_with_email(self,user):
        user = users.get_user(user)
        self.enter_email(user["email"])
        self.click_continue_button()

    def login_with_phone(self,user):
        user = users.get_user(user)
        self.enter_email(user["phone"])
        self.click_continue_button()

    def login_with_password(self,user):
        self.insert_password(user)
        self.click_login_button()

    def login(self, user):
        self.login_with_email(user)
        self.login_with_password(user)

    def forgot_password(self, user):
        self.click_forgot_password_button()
        self.insert_account_if_no_value(user)
        # Temp condition
        if self.is_element_visible(*self.login_page_locator.CVF_CAPTCHA_IMG):
            self.fail(msg="The graphic recognition module has not been developed yet.")
        self.insert_otp()
        self.insert_two_password_check(user)
    
