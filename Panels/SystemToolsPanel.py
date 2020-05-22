from time import sleep
from selenium.webdriver import Chrome 
from selenium.webdriver.remote.webelement import WebElement

from Views.FirmwareUpgradeView import FirmwareUpgradeView
from Views.BackupAndRestoreView import BackupAndRestore

class SystemToolsPanel(object):
    def __init__(self, driver: Chrome):
        self.driver = driver
    
    def NavigateToFirmwareUpgrade(self) -> (FirmwareUpgradeView, str):
        try:
            btnFWUpgrade: WebElement = self.driver.find_element_by_link_text("Firmware Upgrade")
            btnFWUpgrade.click()
            print("Opening Firmware Upgrade View...")
            sleep(2)
            return (FirmwareUpgradeView(self.driver), None)
        except Exception as ex:
            return (None, str(ex))

    def NavigateTo_BackupAndRestore(self) -> (BackupAndRestore, str):
        try:
            btnBackupAndRestore: WebElement = self.driver.find_element_by_link_text("Backup & Restore")
            btnBackupAndRestore.click()
            sleep(2)
            return (BackupAndRestore(self.driver), None)
        except Exception as ex:
            return (None, str(ex))