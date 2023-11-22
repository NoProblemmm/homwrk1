from selenium.webdriver.common.by import By
import time

from fw.web.any_page import AnyPage


class Locator:
    btn_requests = (By.XPATH, '//div[@data-anchor="Requests"]')
    btn_top_menu_my = (By.XPATH, '//div[@data-anchor="Requests"]/..//div[@data-anchor="TopMenuMy"]')


class Main(AnyPage):

    def click_my_request(self):
        self.move_to_element(Locator.btn_requests)
        time.sleep(0.5)
