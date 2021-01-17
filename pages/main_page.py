import time
from selenium.webdriver.common.keys import Keys


from pages.base_page import BasePage
from pages.login_page import LoginPage
from utils.locators import *
from utils.lang import main as LANG_OF_MAIN
from utils import users


class MainPage(BasePage):

    def setUp(self):
        self.main_page_locator = MainPageLocators

        super().setUp()

    def verify_elements_of_login_on_main_page(self):
        self.assert_element_present(*self.main_page_locator.ACCOUNT)
        self.assert_element_present(*self.main_page_locator.SIGNUP)
        self.assert_element_present(*self.main_page_locator.LOGIN)

    def verify_valid_login_by_url(self):
        verification_patterns_in_url = ['ref_=nav_custrec_signin','ap/signin']
        get_url = self.driver.current_url
        gotIt = False
        for pattern in verification_patterns_in_url:
            if pattern in get_url:
                gotIt = True
        self.assert_true(gotIt, msg="The verification of URL fail, Got:{}".format(get_url))

    def verify_valid_login_by_content(self):
        self.wait_for_element(*self.main_page_locator.SELECT_LANGUAGE)
        current_lang= self.get_text(*self.main_page_locator.SELECT_LANGUAGE)

        if '繁體中文' in current_lang:
            lang = 'zh-tw'
        elif 'English' in current_lang:
            lang = 'zh-us'
        else:
            lang = self.get_locale_code()

        # Elements on main page 
        self.assert_element_present(*self.main_page_locator.NAV_YOURE_AMAZON)
        # Text on main page
        user = users.get_user("valid_user")        
        get_text_on_nav_youre_amazon = self.get_text(*self.main_page_locator.TEXT_NAV_YOURE_AMAZON)
        get_text_on_nav_account = self.get_text(*self.main_page_locator.TEXT_NAV_ACCOUNT)
        self.assert_true(LANG_OF_MAIN.MAIN[lang]['accountList'].format(user['display_name'])==get_text_on_nav_account, "Text wrong; Got:{};Not:{}".format(get_text_on_nav_account,LANG_OF_MAIN.MAIN[lang]['accountList'].format(user['display_name'])))
        if '的​ ' in get_text_on_nav_youre_amazon:
            get_text_on_nav_youre_amazon = get_text_on_nav_youre_amazon.replace('的​ ','的 ')
        self.assert_true(LANG_OF_MAIN.MAIN[lang]['shortened_name'].format(user['display_name'])==get_text_on_nav_youre_amazon, "Text wrong;  Got:{};Not:{}".format(get_text_on_nav_youre_amazon,LANG_OF_MAIN.MAIN[lang]['shortened_name'].format(user['display_name'])))

    def verify_valid_login(self):
        self.verify_valid_login_by_url()
        self.verify_valid_login_by_content()
        
    def click_sign_in_button(self):
        self.verify_elements_of_login_on_main_page()
        time.sleep(1)
        if self.is_element_visible(*self.main_page_locator.LOGIN):
            self.click(*self.main_page_locator.LOGIN)
        else:
            self.click(*self.main_page_locator.ACCOUNT)

        return LoginPage()

    def verify_remember_me(self):
        '''Not developed yet'''
        pass

