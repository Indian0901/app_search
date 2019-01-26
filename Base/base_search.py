from selenium.webdriver.support.wait import WebDriverWait


class Base_search:
    def __init__(self,driver):
        self.driver = driver

    def search_element(self,loc,timeout=5,poll_frequency=1):
        return WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x:x.find_element(*loc))

    def search_elements(self, loc, timeout=5, poll_frequency=1):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))


    def click_element(self,loc,timeout=5,poll_frequency=1):
        self.search_element(loc,timeout,poll_frequency).click()

    def send_element(self,loc,text,timeout=5,poll_frequency=1):
        self.search_element(loc,timeout,poll_frequency).send_keys(text)