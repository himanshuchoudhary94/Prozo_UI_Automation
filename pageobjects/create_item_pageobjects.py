import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CreateItemPage:
    def __init__(self, driver):
        self.driver = driver

    NAME_TEXT_BOX = (By.CSS_SELECTOR, "[name='name']")
    BRAND_NAME_DROPDOWN_BUTTON = (By.XPATH,
                                  "//body/div[@id='root']/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[2]/span[1]/*[1]")
    BRAND_LIST = (By.CSS_SELECTOR, "[role='option']")
    CATEGORY_LIST = (By.CSS_SELECTOR, "[role='option']")
    CATEGORY_DROPDOWN_BUTTON = (By.XPATH,
                                "//body/div[@id='root']/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/button[2]/span[1]/*[1]")
    SKU_TEXT_BOX = (By.CSS_SELECTOR, "[name='barCode']")
    EAN_TEXT_BOX = (By.CSS_SELECTOR, "[name='ean']")
    UPC_TEXT_BOX = (By.CSS_SELECTOR, "[name='upc']")
    MIN_REORDER_VALUE_TEXT_BOX = (By.CSS_SELECTOR, "[name='minorder']")
    HSN_DROPDOWN_BUTTON = (By.XPATH,
                           "//body/div[@id='root']/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/form[1]/div[1]/div[8]/div[1]/div[1]/div[1]/div[1]/button[2]/span[1]/*[1]")
    HSN_LIST = (By.CSS_SELECTOR, "[role='option']")
    MRP_TEXT_BOX = (By.CSS_SELECTOR, "[name='mrp']")
    UNIT_OF_MEASUREMENT_DROPDOWN = (By.XPATH,
                                    "//body/div[@id='root']/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/form[1]/div[1]/div[10]/div[1]/div[1]/div[1]/div[1]/button[2]/span[1]/*[1]")
    UNIT_OF_MEASUREMENT_LIST = (By.CSS_SELECTOR, "[role='option']")
    WEIGHT_TEXT_BOX = (By.CSS_SELECTOR, "[name='weight']")
    LENGTH_TEXT_BOX = (By.CSS_SELECTOR, "[name='length']")
    BREADTH_TEXT_BOX = (By.CSS_SELECTOR, "[name='width']")
    HEIGHT_TEXT_BOX = (By.CSS_SELECTOR, "[name='height']")
    DESCRIPTION_TEXT_BOX = (By.CSS_SELECTOR, "[name='description']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
    ERROR_MESSAGE_POPUP = (By.CSS_SELECTOR, "#client-snackbar")

    def enter_name(self, name):
        self.driver.find_element(*CreateItemPage.NAME_TEXT_BOX).send_keys(name)

    def select_brand_name(self, brand_name):
        self.driver.find_element(*CreateItemPage.BRAND_NAME_DROPDOWN_BUTTON).click()
        list_of_brands = self.driver.find_elements(*CreateItemPage.BRAND_LIST)
        for brand in list_of_brands:
            if brand.text == brand_name:
                brand.click()
                break

    def select_category(self, category_name):
        self.driver.find_element(*CreateItemPage.CATEGORY_DROPDOWN_BUTTON).click()
        list_of_category = self.driver.find_elements(*CreateItemPage.CATEGORY_LIST)
        for category in list_of_category:
            if category_name in category.text:
                category.click()
                break   #staleelement if not break

    def enter_sku_id(self, sku_id):
        self.driver.find_element(*CreateItemPage.SKU_TEXT_BOX).send_keys(sku_id)

    def enter_ean(self, ean):
        self.driver.find_element(*CreateItemPage.EAN_TEXT_BOX).send_keys(ean)

    def enter_upc(self, upc):
        self.driver.find_element(*CreateItemPage.UPC_TEXT_BOX).send_keys(upc)

    def enter_min_reorder_value(self, min_reorder_value):
        self.driver.find_element(*CreateItemPage.MIN_REORDER_VALUE_TEXT_BOX).send_keys(min_reorder_value)

    def select_hsn(self, hsn_name):
        self.driver.find_element(*CreateItemPage.HSN_DROPDOWN_BUTTON).click()
        list_of_hsn = self.driver.find_elements(*CreateItemPage.HSN_LIST)
        for hsn in list_of_hsn:
            if hsn.text == hsn_name:
                hsn.click()
                break

    def enter_mrp(self, mrp):
        self.driver.find_element(*CreateItemPage.MRP_TEXT_BOX).send_keys(mrp)

    def select_unit_of_measurement(self, unit_name):
        self.driver.find_element(*CreateItemPage.UNIT_OF_MEASUREMENT_DROPDOWN).click()
        list_of_units = self.driver.find_elements(*CreateItemPage.UNIT_OF_MEASUREMENT_LIST)
        for unit in list_of_units:
            if unit.text == unit_name:
                unit.click()
                break

    def enter_weight(self, weight):
        self.driver.find_element(*CreateItemPage.WEIGHT_TEXT_BOX).send_keys(weight)

    def enter_length(self, length):
        self.driver.find_element(*CreateItemPage.LENGTH_TEXT_BOX).send_keys(length)

    def enter_breadth(self, breadth):
        self.driver.find_element(*CreateItemPage.BREADTH_TEXT_BOX).send_keys(breadth)

    def enter_height(self, height):
        self.driver.find_element(*CreateItemPage.HEIGHT_TEXT_BOX).send_keys(height)

    def enter_description(self, description):
        self.driver.find_element(*CreateItemPage.DESCRIPTION_TEXT_BOX).send_keys(description)

    def click_save(self):
        self.driver.find_element(*CreateItemPage.SAVE_BUTTON).click()

    def check_empty_or_not(self):
        if self.driver.find_element(*CreateItemPage.NAME_TEXT_BOX).get_attribute("aria-invalid"):
            return True

    def check_error_message(self):
        time.sleep(1)
        return self.driver.find_element(*CreateItemPage.ERROR_MESSAGE_POPUP).is_displayed()

    def refresh_page(self):
        self.driver.refresh()

    def get_current_url(self):
        self.driver.get(self.driver.current_url)

    def explicit_wait_for_error_pop_up(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.driver.find_element(*CreateItemPage.ERROR_MESSAGE_POPUP)))

