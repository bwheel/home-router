from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement

class FirmwareUpgradeView(object):
    def __init__(self, driver: Chrome):
        self.driver = driver
    
    def IsUpdateAvailable(self)-> (bool, str):
        try:
            btnCheckForUpdate: WebElement = self.driver.find_element_by_id('check-upgrade')
            btnCheckForUpdate.click()
            print("Checking to see if firmware is up to date...")
            sleep(5)
            lblResult: WebElement = self.driver.find_element_by_id('check-result')
            return (lblResult.text != "Your firmware is up to date", lblResult.text)
        except Exception as ex:
            return (None, str(ex))

    def getFirmwareVersion(self) -> (str, str):
        try:
            lblFirmwareVersion: WebElement = self.driver.find_element_by_id('firmware_version')
            fwVersion: str = str(lblFirmwareVersion.get_attribute('snapshot'))
            return(fwVersion, None)
        except Exception as ex:
            return (None, str(ex))
        
    def getHardwareVersion(self) -> (str, str):
        try:
            lblHardwareVersion = self.driver.find_element_by_id('hardware_version')
            hwVersion = lblHardwareVersion.get_attribute('snapshot')
            return (hwVersion, None)
        except Exception as ex:
            return (None, str(ex))
        
    def installUpdatedFirmware(self) -> (bool, str):
        pass