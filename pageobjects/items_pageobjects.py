from selenium.webdriver.common.by import By


class ItemsPage:
    def __init__(self, driver):
        self.driver = driver

    CREATE_NEW_ITEM_BUTTON = (By.XPATH, "//span[text()='Create New Item']")

    def click_create_new_item(self):
        self.driver.find_element(*ItemsPage.CREATE_NEW_ITEM_BUTTON).click()

    def check_create_new_item_visibility(self):
        return self.driver.find_element(*ItemsPage.CREATE_NEW_ITEM_BUTTON).is_displayed()