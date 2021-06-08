import time

import pytest

from pageobjects.create_item_pageobjects import CreateItemPage
from pageobjects.home_pageobjects import HomePage
from pageobjects.items_pageobjects import ItemsPage
from pageobjects.login_objects import LoginPage
from testdata.login_data import LoginPageData
from utilities.base_class import BaseClass
from pageobjects.domain_pageobjects import DomainPage


class TestLogin(BaseClass):

    def test_check_correct_website_opened(self, getLoginData):
        """This function tests whether the website opened is correct or not"""

        assert self.driver.title == getLoginData["title"], "%s is incorrect Website" % self.driver.title

    def test_check_domain_name_entry(self, getLoginData):
        """This function tests whether domain entry point is passed for positive test scenario"""

        domain_page = DomainPage(self.driver)
        domain_page.enter_domain(getLoginData['domain_name'])
        domain_page.click_continue()
        login_page = LoginPage(self.driver)
        assert login_page.check_sign_in_visibility(), "Unable to find to the sign in window"

    def test_check_correct_login_password(self, getLoginData):
        """This function tests whether correct login password is passed for positive test scenario"""

        login_page = LoginPage(self.driver)
        login_page.enter_mobile_number(getLoginData['username'])
        login_page.enter_password(getLoginData['password'])
        login_page.click_sign_in()
        home_page = HomePage(self.driver)
        assert home_page.items_menu_visibility(), "Unable to find to the sign in window"

    def test_traverse_to_create(self, getLoginData):
        """This function tests traversal to create new Item"""

        home_page = HomePage(self.driver)
        home_page.click_items_menu()
        assert home_page.items_sub_menu_visibility(), "Unable to find items sum menu"
        home_page.click_sub_menu_items()
        items_page = ItemsPage(self.driver)
        assert items_page.check_create_new_item_visibility(), "Unable to find create new item button"

    def test_empty_submission(self):
        """This function tests whether empty form is saved or not"""

        items_page = ItemsPage(self.driver)
        items_page.click_create_new_item()
        create_item_page = CreateItemPage(self.driver)
        create_item_page.click_save()
        assert create_item_page.check_empty_or_not(), "Empty Error didn't occur"

    def test_wrong_weight_type(self):
        """This function tests whether alphabetical submission of weight saves the form"""

        create_item_page = CreateItemPage(self.driver)
        create_item_page.refresh_page()
        time.sleep(2)
        create_item_page.enter_name("Himanshu")
        create_item_page.select_brand_name("Oswaal Books")
        create_item_page.select_category("All Competition Books")
        create_item_page.enter_sku_id("1234")
        create_item_page.select_hsn("49011010 (0%)")
        create_item_page.enter_mrp("120")
        create_item_page.select_unit_of_measurement("Grams")
        create_item_page.enter_weight("QWERTY")
        create_item_page.enter_length("100")
        create_item_page.enter_breadth("100")
        create_item_page.enter_height("100")
        create_item_page.enter_description("ABC")
        create_item_page.click_save()
        assert create_item_page.check_error_message(), "Wrong value accepted"

    def test_wrong_length_type(self):
        """This function tests whether alphabetical submission of length saves the form"""

        create_item_page = CreateItemPage(self.driver)
        create_item_page.refresh_page()
        time.sleep(2)
        create_item_page.enter_name("Himanshu")
        create_item_page.select_brand_name("Oswaal Books")
        create_item_page.select_category("All Competition Books")
        create_item_page.enter_sku_id("1234")
        create_item_page.select_hsn("49011010 (0%)")
        create_item_page.enter_mrp("120")
        create_item_page.select_unit_of_measurement("Grams")
        create_item_page.enter_weight("100")
        create_item_page.enter_length("QWERTY")
        create_item_page.enter_breadth("100")
        create_item_page.enter_height("100")
        create_item_page.enter_description("ABC")
        create_item_page.click_save()
        assert create_item_page.check_error_message(), "Wrong value accepted"

    def test_wrong_breadth_type(self):
        """This function tests whether alphabetical submission of breadth saves the form"""

        create_item_page = CreateItemPage(self.driver)
        create_item_page.refresh_page()
        time.sleep(2)
        create_item_page.enter_name("Himanshu")
        create_item_page.select_brand_name("Oswaal Books")
        create_item_page.select_category("All Competition Books")
        create_item_page.enter_sku_id("1234")
        create_item_page.select_hsn("49011010 (0%)")
        create_item_page.enter_mrp("120")
        create_item_page.select_unit_of_measurement("Grams")
        create_item_page.enter_weight("100")
        create_item_page.enter_length("100")
        create_item_page.enter_breadth("QWERTY")
        create_item_page.enter_height("100")
        create_item_page.enter_description("ABC")
        create_item_page.click_save()
        assert create_item_page.check_error_message(), "Wrong value accepted"

    def test_wrong_height_type(self):
        """This function tests whether alphabetical submission of height saves the form"""

        create_item_page = CreateItemPage(self.driver)
        create_item_page.refresh_page()
        time.sleep(2)
        create_item_page.enter_name("Himanshu")
        create_item_page.select_brand_name("Oswaal Books")
        create_item_page.select_category("All Competition Books")
        create_item_page.enter_sku_id("1234")
        create_item_page.select_hsn("49011010 (0%)")
        create_item_page.enter_mrp("120")
        create_item_page.select_unit_of_measurement("Grams")
        create_item_page.enter_weight("100")
        create_item_page.enter_length("100")
        create_item_page.enter_breadth("100")
        create_item_page.enter_height("QWERTY")
        create_item_page.enter_description("ABC")
        create_item_page.click_save()
        assert create_item_page.check_error_message(), "Wrong value accepted"


    @pytest.fixture(params=LoginPageData.LOGIN_PAGE_DATA)
    def getLoginData(self, request):
        return request.param
