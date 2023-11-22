from Test.t_base import TestsBase


class PreCondition(TestsBase):

    def setup_class(self):
        pass

    def teardown_class(self):
        self.APP.driver_area.stop_driver()

    def setup_method(self):
        self.APP.driver_area.start_driver()
        self.APP.any_page.open_main_page()

    def teardown_method(self):
        self.APP.driver_area.stop_driver()