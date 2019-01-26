from Base.base_search import Base_search
import Page

class Page_set(Base_search):
    def __init__(self,driver):
        Base_search.__init__(self,driver)

    def click_search(self):
        self.click_element(Page.search_id)