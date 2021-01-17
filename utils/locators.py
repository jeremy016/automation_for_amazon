from selenium.webdriver.common.by import By


# Seperate web objects by page name

class MainPageLocators(object): 
    A_PAGE = ( 'a-page',By.ID)
    ACCOUNT = ( 'nav-link-accountList',By.ID)
    SIGNUP = ( '#nav-signin-tooltip > div > a',By.CSS_SELECTOR)
    LOGIN = ( '#nav-signin-tooltip > a',By.CSS_SELECTOR)
    NAV_YOURE_AMAZON = ( 'nav-your-amazon',By.ID)
    NAV_YOURE_SOTRE = ( 'nav-subnav', By.ID)
    TEXT_NAV_YOURE_AMAZON = ( 'nav-your-amazon-text',By.ID)
    TEXT_NAV_ACCOUNT = ( 'nav-link-accountList-nav-line-1',By.ID)
    SELECT_LANGUAGE = ( '#icp-touch-link-language > span.icp-color-base',By.CSS_SELECTOR)

class LoginPageLocators(object):
    # locators of email page
    LINK_LOGO = ( 'a.a-link-nav-icon', By.CSS_SELECTOR)
    ICON_LOGO = ( 'i.a-icon.a-icon-logo', By.CSS_SELECTOR)
    TITLE_LOGIN = ( 'h1.a-spacing-small', By.CSS_SELECTOR)
    LABEL_EMAIL = ( 'label.a-form-label' , By.CSS_SELECTOR)
    LEGAL_TEXT = ( 'legalTextRow', By.ID)
    CONDITIONS_OF_USE = ( '#legalTextRow > a:nth-child(1)', By.CSS_SELECTOR)
    PRIVACY_NOTICE = ( '#legalTextRow > a:nth-child(2)', By.CSS_SELECTOR)
    NEED_HELP = ( 'span.a-expander-prompt', By.CSS_SELECTOR)
    OTHER_ISSUES = ( 'ap-other-signin-issues-link', By.ID)
    NEW_TO_AMAZON = ( 'div.a-divider.a-divider-break', By.CSS_SELECTOR)
    SUBMIT_CREATE_ACCOUNT = ( 'createAccountSubmit', By.ID)
    EMAIL = ( 'ap_email', By.ID)
    CONTINUE = ( 'continue', By.ID)
    # locators of password page
    LABEL_PASSWORD = ( 'div.a-column.a-span5> label.a-form-label' , By.CSS_SELECTOR)
    EMAIL_TEXT = ( 'div.a-row.a-spacing-base > span', By.CSS_SELECTOR)
    CHANGE_LOGIN = ( 'ap_change_login_claim', By.ID)
    PASSWORD = ( 'ap_password', By.ID)
    SUBMIT = ( 'signInSubmit', By.ID)
    TEXT_SUBMIT = ( 'auth-signin-button-announce', By.ID)
    ERROR_MESSAGE = ( 'message_error', By.ID)
    FORGOT_PASSWORD = ( 'auth-fpp-link-bottom', By.ID)
    KEEP_SIGNED_IN_CHECKBOX = ( 'input[name=rememberMe]',By.CSS_SELECTOR)
    KEEP_SIGNED_IN_LABEL = ( 'span.a-label.a-checkbox-label',By.CSS_SELECTOR)
    KEEP_SIGNED_IN_DETAIL= ( 'remember_me_learn_more_link', By.ID)
    # authentication required
    AUTH_CAPTCHA_IMAGE = ( 'auth-captcha-image-container',By.ID)
    CVF_CAPTCHA_IMG = ( '.a-section.a-text-center.cvf-captcha-img',By.CSS_SELECTOR)
    EMAIL_CVF = ( '#cvf-page-content > div > div > div:nth-child(1) > form > div:nth-child(2) > input', By.CSS_SELECTOR)
    CONTINUE_AUTHENTICATION_REQUIRED = ( '#a-autoid-0 > span > input', By.CSS_SELECTOR)
    # locators of alert
    AUTH_ERROR_MESSAGE_BOX = ( 'auth-error-message-box', By.ID)
    EMAIL_CONTENT_ALERT = ( '#auth-email-missing-alert > div > div.a-alert-content', By.CSS_SELECTOR)
    PASSWORD_CONTENT_ALERT = ( '#auth-password-missing-alert > div > div.a-alert-content', By.CSS_SELECTOR)
    AUTH_ERROR_MESSAGE_ICON = ( '#auth-error-message-box > .a-box-inner.a-alert-container > i.a-icon.a-icon-alert', By.CSS_SELECTOR)
    AUTH_ERROR_MESSAGE_HEADER = ( '#auth-error-message-box > .a-box-inner.a-alert-container > h4.a-alert-heading', By.CSS_SELECTOR)
    AUTH_ERROR_MESSAGE_CONTENT = ( '#auth-error-message-box > div > div > ul > li > span.a-list-item', By.CSS_SELECTOR)
    # ap_fpp_password
    AP_FPP_PASSWORD = ( 'ap_fpp_password', By.ID)
    AP_FPP_PASSWORD_CHECK = ( 'ap_fpp_password_check', By.ID)
    