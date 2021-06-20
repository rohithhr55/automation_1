class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_xpath = "/html/body/div[1]/div[1]/a[2]"
        self.logout_xpath = "/html/body/div[1]/div[1]/div[10]/ul/li[3]/a"

    def welcome(self):
        self.driver.find_element_by_xpath(self.welcome_xpath).click()

    def logout(self):
        self.driver.find_element_by_xpath(
            self.logout_xpath).click()

