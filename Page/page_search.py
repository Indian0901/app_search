from Base.base_search import Base_search
import Page

class Page_search(Base_search):
    def __init__(self,driver):
        Base_search.__init__(self,driver)

    def send_text(self,text):
        self.send_element(Page.text_id,text)

    def res_list(self):
        return [i.text for i in self.search_elements(Page.res_id)]