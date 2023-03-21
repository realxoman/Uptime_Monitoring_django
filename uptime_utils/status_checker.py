from uptime_utils.domain_checker import DomainChecker

class StatusChecker:

    def __init__(self, url) -> None:
        self.url = url
    
    def check_status(self):
        self.checker = DomainChecker.send_request(self.url)
        self.status = self.checker.status_code
        return 
    
    def validation(self):
        if self.status == 200:
            return True
        return False