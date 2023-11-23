from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from fw.web.any_page import AnyPage


class CreateRequest(AnyPage):

    def new_design(self):
        try:
            self.find_element((By.XPATH, '//*[@id="vue_common_placeholder"]'))
            return True
        except:
            return False

    def create_new_request(self):
        time.sleep(9)
        if self.new_design():
            self.click_element((By.XPATH, '//*[@id="vue_common_placeholder"]'))
        self.click_element((By.XPATH, '//div[@class="header__button"]'))
        time.sleep(4)
        self.click_element((By.XPATH, '//div[@id="option-new"]'))

    def selection_of_the_gandiva_department(self):
        time.sleep(4)
        self.click_element((By.XPATH, '//*[@id="Department_chosen"]'))
        time.sleep(4)
        self.send_keys((By.XPATH, '//div[@id="Department_chosen"]//input[@class="chosen-search-field"]'),
                                    ('Отдел тестирования Гандивы', Keys.ENTER))

    def choosing_a_category(self):
        self.click_element((By.XPATH, '//div[@id="Category_chosen"]'))
        time.sleep(2)
        self.send_keys((By.XPATH, '//div[@id="Category_chosen"]//input[@class="chosen-search-field"]'),
                                    ('Программное обеспечение', Keys.ENTER))

    def choosing_type(self):
        self.click_element((By.XPATH, '//*[@id="RequestType_chosen"]'))
        self.send_keys((By.XPATH, '//div[@id="RequestType_chosen"]//input[@class="chosen-search-field"]'),
                                    ('MS GANDIVA', Keys.ENTER))

    def choosing_job_type(self):
        self.click_element((By.XPATH, '//*[@id="JobType_chosen"]'))
        self.send_keys((By.XPATH, '//div[@id="JobType_chosen"]//input[@class="chosen-search-field"]'),
                                    ('Тестовый_Тип_1', Keys.ENTER))

    def input_field(self):
        input_field = self.find_element((By.XPATH, '//*[@id="cke_1_contents"]/iframe'))
        time.sleep(2)
        self.get_driver().switch_to.frame(input_field)
        time.sleep(2)
        self.send_keys((By.XPATH, '//*[@class="cke_editable cke_editable_themed cke_contents_ltr"]'), 'test')
        time.sleep(2)
        self.get_driver().switch_to.default_content()

    def add_a_cordinator(self, user, result):
        self.click_element((By.XPATH, '//*[@data-handler="request_agreement_build"]'))
        time.sleep(2)
        self.click_element((By.XPATH, '//div[@id="get_user_request_chosen"]'))
        time.sleep(2)
        self.send_keys((By.XPATH, '//div[@id="get_user_request_chosen"]//input[@class="chosen-search-field"]'), user)
        time.sleep(2)
        self.click_element((By.XPATH, f'//*[@id="get_user_request_chosen"]/div/ul/li[{result}]'))