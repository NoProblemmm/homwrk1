
from Test.pre_condition import PreCondition


class TestMain(PreCondition):

   def test_first_test(self):
       self.APP.log_in.open_main_page()
