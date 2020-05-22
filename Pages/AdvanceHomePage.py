from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement

from Panels.SystemToolsPanel import SystemToolsPanel

class AdvanceHomePage(object):
    def __init__(self, driver: Chrome):
        self.driver = driver
    
    def Expand_SystemTools(self) -> (SystemToolsPanel, str):
        try:
            btnSystemTools: WebElement = self.driver.find_element_by_id('menu-advanced-system-tools-li')
            btnSystemTools.click()
            print("Expanding System tools panel...")
            sleep(0.25)
            return (SystemToolsPanel(self.driver), None)
        except Exception as ex:
            return (None, str(ex))