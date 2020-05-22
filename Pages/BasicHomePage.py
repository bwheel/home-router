from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from Pages.AdvanceHomePage import AdvanceHomePage

class BasicHomePage(object):
    def __init__(self, driver: Chrome):
        self.driver = driver
    
    def NavigateTo_AdvancedPage(self) -> (str, AdvanceHomePage):
        try:
            divTopNav: WebElement = self.driver.find_element_by_id('top-nav')
            btnAdvanced: WebElement = divTopNav.find_element_by_link_text('Advanced')
            btnAdvanced.click()
            print("Navigating to Advanced tab...")
            sleep(1.5)
            return (AdvanceHomePage(self.driver), None)
        except Exception as ex:
            return (None, str(ex))        

        