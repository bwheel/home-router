from selenium.webdriver import Chrome

class BackupAndRestore(object):
    def __init__(self, driver: Chrome):
        self.driver = driver
    
    def PerformBackup(self) -> (str, bool):
        pass