from Page.page_set import Page_set
from Page.page_search import Page_search

class Get_obj:
    def __init__(self,driver):
        self.driver = driver

    def set_obj(self):
        return Page_set(self.driver)
    def search_obj(self):
        return Page_search(self.driver)