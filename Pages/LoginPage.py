from time import sleep
from selenium.webdriver import Chrome 
from selenium.webdriver.remote.webelement import WebElement
from Pages.BasicHomePage import BasicHomePage

class LoginPage(object):

    def __init__(self, driver: Chrome):
        self.driver = driver

    def Login(self, password: str ) -> (BasicHomePage, str):
        try:
            # Scrape elements
            form: WebElement = self.driver.find_element_by_id('form-login')
            divWrap: WebElement = form.find_element_by_class_name('widget-wrap')
            inputPassword: WebElement = divWrap.find_element_by_tag_name('input')
            btnSubmit: WebElement = form.find_element_by_id('login-btn')
            
            #interact with UI.
            inputPassword.send_keys(password)
            btnSubmit.click()
            print("Logging in...")
            sleep(6.5)
            return (BasicHomePage(self.driver), None)
        except Exception as ex:
            return (None, str(ex))
        
        