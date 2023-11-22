from selenium.webdriver.common.by import By
import time
from fw.web.web_base import WebBase


class AnyPage(WebBase):

    def open_main_page(self):
        self.get_driver().get(self.manager.group_data.base_url_web)

    def go_to_requests(self):
        self.click_element((By.XPATH, '//*[@data-anchor="Requests"]'))

    def go_to_request_creats(self, number_request):
        time.sleep(2)
        self.get_driver().get(f'https://web-test-compose.gandiva.ru/Request/Edit/{number_request}')
