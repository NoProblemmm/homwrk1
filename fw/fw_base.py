

class FWBase:

    def __init__(self, ApplicationManager):
        self.manager = ApplicationManager

    def request_logs(self, type='', url='', headers='', body="", status_code='', response_text='', params=''):
        pass