from selenium.webdriver.common.by import By
import allure
from Test.pre_condition import PreCondition
import time

class TestRequests(PreCondition):

    def test_request(self):
        self.APP.any_page.open_main_page()
        self.APP.log_in.login_password()
        self.APP.any_page.go_to_requests()
        self.APP.create_request.create_new_request()
        self.APP.create_request.selection_of_the_gandiva_department()
        self.APP.create_request.choosing_a_category()
        self.APP.create_request.choosing_type()
        self.APP.create_request.choosing_job_type()
        self.APP.create_request.input_field()
        for result in range(2):
            result += 1
            self.APP.create_request.add_a_cordinator('boss', result)
        self.APP.edit_request.save_request()
        number_request = self.APP.edit_request.get_request()
        print(number_request)
        self.APP.log_in.logout()
        self.APP.log_in.login_password(self.APP.group_data.users['boss1']['log'],
                                       self.APP.group_data.users['boss1']['pass'])
        self.APP.any_page.go_to_request_creats(number_request)
        self.APP.edit_request.to_approve_request()
        boss1 = self.APP.edit_request.coordinator_status(self.APP.group_data.users['boss1']['id'])
        self.APP.log_in.logout()
        self.APP.log_in.login_password(self.APP.group_data.users['boss2']['log'],
                                       self.APP.group_data.users['boss2']['pass'])
        self.APP.any_page.go_to_request_creats(number_request)
        self.APP.edit_request.reject_request()
        boss2 = self.APP.edit_request.coordinator_status(self.APP.group_data.users['boss2']['id'])

        assert self.APP.edit_request.request_status() == 'Отклонена'
        assert 'Согласовано' in boss1
        assert 'Отклонено' in boss2

    def test_request_job(self):
        self.APP.any_page.open_main_page()
        self.APP.log_in.login_password()
        self.APP.any_page.go_to_requests()
        self.APP.create_request.create_new_request()
        self.APP.create_request.selection_of_the_gandiva_department()
        self.APP.create_request.choosing_a_category()
        self.APP.create_request.choosing_type()
        self.APP.create_request.choosing_job_type()
        self.APP.create_request.input_field()
        for result in range(2):
            result += 1
            self.APP.create_request.add_a_cordinator('boss1', result)
        self.APP.edit_request.save_request()
        number_request = self.APP.edit_request.get_request()
        self.APP.log_in.logout()
        self.APP.log_in.login_password(self.APP.group_data.users['boss1']['log'],
                                       self.APP.group_data.users['boss1']['pass'])
        self.APP.any_page.go_to_request_creats(number_request)
        self.APP.edit_request.to_approve_request()
        self.APP.edit_request.save_request()
        boss1 = self.APP.edit_request.coordinator_status(self.APP.group_data.users['boss1']['id'])
        self.APP.log_in.logout()
        self.APP.log_in.login_password(self.APP.group_data.users['boss2']['log'],
                                       self.APP.group_data.users['boss2']['pass'])
        self.APP.any_page.go_to_request_creats(number_request)
        self.APP.edit_request.reject_request()
        self.APP.edit_request.save_request()
        boss2 = self.APP.edit_request.coordinator_status(self.APP.group_data.users['boss2']['id'])

        assert self.APP.edit_request.request_status() == 'Согласовано'
        assert 'Отклонено' in boss1
        assert 'Согласовано' in boss2

    def test_users_transfer_to_verification(self):
        self.APP.any_page.open_main_page()
        self.APP.log_in.login_password()
        self.APP.any_page.go_to_requests()
        self.APP.create_request.selection_of_the_gandiva_department()
        self.APP.create_request.choosing_a_category()
        self.APP.create_request.choosing_type()
        self.APP.create_request.choosing_job_type()
        self.APP.edit_request.save_request()
        first_user_button_assign_yourself = \
                                self.APP.edit_request.presence_of_the_button(self.APP.group_data.button_assign_yourself)
        number_request = self.APP.edit_request.get_request()
        self.APP.log_in.logout()
        self.APP.log_in.login_password(self.APP.group_data.users['user3']['log'],
                                       self.APP.group_data.users['boss3']['pass'])
        self.APP.any_page.go_to_request_creats(number_request)
        second_button_assign_yourself =\
                                self.APP.edit_request.presence_of_the_button(self.APP.group_data.button_assign_yourself)
        self.APP.edit_request.assign_yourself()
        self.APP.edit_request.save_request()
        second_user_button_conduct_a_check =\
                                       self.APP.edit_request.presence_of_the_button(self.APP.group_data.conduct_a_check)
        self.APP.edit_request.go_to_examination()
        self.APP.edit_request.save_request()
        second_user_button_to_work =\
                                self.APP.edit_request.presence_of_the_button(self.APP.group_data.button_at_work)
        self.APP.log_in.logout()
        self.APP.any_page.open_main_page()
        self.APP.log_in.login_password()
        self.APP.any_page.go_to_request_creats(number_request)
        first_user_button_to_work = \
            self.APP.edit_request.presence_of_the_button(self.APP.group_data.button_at_work)
        self.APP.edit_request.evaluate_the_work()
        self.APP.edit_request.save_request()


        assert first_user_button_to_work
        assert first_user_button_assign_yourself
