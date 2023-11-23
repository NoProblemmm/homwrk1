from data.group_data import GroupData
from fw.api.request.api_request import Request
from fw.web.any_page import AnyPage
from fw.web.driver_area import DriverArea
from fw.web.logiin.log_in import Login
from fw.web.main import Main
from fw.web.request.create_request import CreateRequest
from fw.web.request.edit_request import EditRequest


class ApplicationManager:

    group_data = GroupData

    def __init__(self):

        self.driver_area = DriverArea()
        self.any_page = AnyPage(self)
        self.log_in = Login(self)
        self.main = Main(self)
        self.create_request = CreateRequest(self)
        self.edit_request = EditRequest(self)
        self.api_request = Request()