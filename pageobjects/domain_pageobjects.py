from selenium.webdriver.common.by import By


class DomainPage:
    def __init__(self, driver):
        self.driver = driver

    DOMAIN_TEXTBOX = (By.CSS_SELECTOR, "input[name='domain']")
    CONTINUE_BUTTON = (By.XPATH, "//span[text()='Continue']")

    def enter_domain(self, domain_name):
        self.driver.find_element(*DomainPage.DOMAIN_TEXTBOX).clear()
        self.driver.find_element(*DomainPage.DOMAIN_TEXTBOX).send_keys(domain_name)

    def click_continue(self):
        self.driver.find_element(*DomainPage.CONTINUE_BUTTON).click()