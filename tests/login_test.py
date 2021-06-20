from selenium import webdriver
import pytest

from pages.homepage import HomePage
from pages.loginpage import LoginPage
from utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class Test_login():

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.enter_login()
        driver.get_screenshot_as_file("C:/Users/rohit/PycharmProjects/pythonProject2/automation_1/screenshots" + "ac1"+".png")
        driver.implicitly_wait(5)

    def test_logout(self):
        driver = self.driver
        homepage = HomePage(driver)

        homepage.welcome()
        homepage.logout()
