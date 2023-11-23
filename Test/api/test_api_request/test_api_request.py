import allure
from Test.api.api_pre_condition import ApiPreConditions

import pytest


@allure.feature('Api')
@allure.story('Request')
class TestApiRequests(ApiPreConditions):

    def test_requests_2(self, user, text, expected):

        login = self.APP.group_data.users['user1']['log']
        password = self.APP.group_data.users['user1']['pass']

        description = f"API Test request {self.APP.time.get_date_time_for_sql_increased_x_days()} -- {text}"

        self.APP.api_token.get_token(login, password)
        body = {
            "Department": {"id": 38},
            "Category": {"id": 489},
            "RequestType": {"id": 2552},
            "JobType": {"id": 13728},
            "Description": description,
            "Approvers": (
                {"id": "",
                "IsUserAdded": True},
                {"id": "",
                "IsUserAdded": True}
        )
        }

        response = self.APP.api_requests.post_requests(body)
        id_request = response['id']

        login = self.APP.group_data.users['boss1']['log']
        password = self.APP.group_data.users['boss1']['pass']
        self.APP.api_token.get_token(login, password)

