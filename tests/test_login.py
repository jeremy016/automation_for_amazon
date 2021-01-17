import time
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage


# In this module, there should be test cases.

class TestLogin(MainPage,LoginPage):

    def setUp(self):
        super().setUp()
        self.amazonURL = "https://www.amazon.com/"
        self.homepageURL = "https://www.google.com/"
        self.locale = self.get_locale()

        self.open(self.amazonURL)
        self.click_sign_in_button()
            
    def test_all_the_elements_and_controls_on_the_login_page(self):
        ''' Verify that all the elements and controls including text-boxes, buttons, and links are present on the Login page '''

        self.verify_elements_of_login_on_account_input_page(self.locale)
        self.login_with_email("valid_user")
        self.verify_elements_of_login_on_password_input_page(self.locale)
        
    def test_login_with_a_vaild_username_and_valid_password(self):
        '''Verify if a user will be able to login with a valid username and valid password.'''

        self.login("valid_user")
        self.verify_valid_login()

    def test_forgot_password(self):
        '''Verify the ‘Forgot Password’ functionality'''

        self.login_with_email("valid_user")
        self.forgot_password("valid_user")
        self.verify_valid_login()

    def test_the_messages_for_invalid_account(self):
        '''Verify the error messages with invalid account.'''

        # Invalid eamil format        
        self.login_with_email("invalid_user")
        self.verify_auth_error_mssage_when_submit_with(self.locale,'invalid_email_format')
        # Invalid phonoe format
        self.login_with_phone("invalid_user")
        self.verify_auth_error_mssage_when_submit_with(self.locale,'invalid_phone_format')

    def test_remember_me(self):
        '''Verify the 'remember me' functionality'''

        self.login_with_email("valid_user")
        self.select_remember_me()
        self.login_with_password("valid_user")
        self.verify_remember_me()
        
    def test_password_is_in_masked_form_when_entered(self):
        '''Verify that the password is in masked form when entered'''

        self.login_with_email("valid_user")
        self.insert_password("valid_user")
        self.verify_password_is_in_masked()

    def test_the_enter_key_of_keyboard_is_working(self):
        '''Verify that the user is able to login by entering valid credentials and pressing Enter key.'''
        
        self.login_with_email("valid_user")
        self.insert_password("valid_user")
        self.sendKeys('ENTER')
        self.verify_valid_login()

    def test_closing_the_browser_should_not_logout(self):
        '''Verify that closing the browser should not log-out an authenticated user. Launching the application should lead the user to login state only. '''
        
        self.login("valid_user")
        self.verify_valid_login()
        self.save_cookies(name="cookies.txt")
        self.driver.close()
        super().setUp()
        self.open(self.homepageURL)
        self.load_cookies(name="cookies.txt")
        self.open(self.amazonURL)
        self.verify_valid_login_by_content()

    def test_messages_for_login_with_field_as_blank(self):    
        '''Verify that the validation message gets displayed in case the user leaves the username or password field as blank.'''
        
        # Empty account
        self.click_continue_button()
        self.verify_error_message_without_account(self.locale)
        self.login_with_email("valid_user")
        # Empty password
        self.click_login_button()
        self.verify_error_message_without_password(self.locale)
        
    def test_back_button_doesnot_logout_user(self):
        '''Verify that once logged in, clicking the back button doesn’t logout the user.'''

        self.login("valid_user")
        self.verify_valid_login()
        self.driver.back()
        # self.driver.get(self.amazonURL)
        self.open(self.amazonURL)
        self.verify_valid_login_by_content()

    def test_can_not_login_with_a_valid_username_and_invalid_passord(self):
        '''Verify that the user is not able to login with an valid username and invalid password.'''
        
        self.login_with_email("valid_user")        
        self.login_with_password("invalid_user")
        self.verify_auth_error_mssage_when_submit_with(self.locale,'wrong_password')



