from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    MOBILE_TEXTBOX = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_TEXTBOX = (By.CSS_SELECTOR, "input[name='password']")
    SIGN_IN_BUTTON = (By.XPATH, "//span[text()='Sign In']")
    GO_BACK_BUTTON = (By.CSS_SELECTOR, "//span[text()='Go Back']")


    def enter_mobile_number(self, mobile_number):
        self.driver.find_element(*LoginPage.MOBILE_TEXTBOX).send_keys(mobile_number)

    def enter_password(self, password):
        self.driver.find_element(*LoginPage.PASSWORD_TEXTBOX).send_keys(password)

    def click_sign_in(self):
        self.driver.find_element(*LoginPage.SIGN_IN_BUTTON).click()

    def click_go_back(self):
        self.driver.find_element(*LoginPage.GO_BACK_BUTTON).click()

    def check_sign_in_visibility(self):
        return self.driver.find_element(*LoginPage.SIGN_IN_BUTTON).is_displayed()











