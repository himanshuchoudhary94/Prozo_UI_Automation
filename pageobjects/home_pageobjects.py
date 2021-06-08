import time

from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    ITEMS_MENU = (By.LINK_TEXT, "Items")
    ITEMS_SUB_MENU = (By.CSS_SELECTOR, "[href='/items']")

    def click_items_menu(self):
        self.driver.find_element(*HomePage.ITEMS_MENU).click()

    def click_sub_menu_items(self):
        self.driver.find_element(*HomePage.ITEMS_SUB_MENU).click()

    def items_menu_visibility(self):
        # time.sleep(1)
        return self.driver.find_element(*HomePage.ITEMS_MENU).is_displayed()

    def items_sub_menu_visibility(self):
        # time.sleep(1)
        return self.driver.find_element(*HomePage.ITEMS_SUB_MENU).is_displayed()