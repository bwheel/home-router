import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Pages.LoginPage import LoginPage
from Pages.BasicHomePage import BasicHomePage
from Pages.AdvanceHomePage import AdvanceHomePage
from Panels.SystemToolsPanel import SystemToolsPanel
from Views.BackupAndRestoreView import BackupAndRestore
from Views.FirmwareUpgradeView import FirmwareUpgradeView

def load_credentials():
    try:
        with open(".credentials") as f:
            return f.readline()
    except Exception as ex:
        print("Must have the credentials file with the password in it to login to wifi router.")
        return None



def main():
    password = load_credentials()
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--headless")
    options.add_argument("--log-level=3")  # fatal
    #options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.get("http://tplinkwifi.net/webpages/login.html")
    
    print("Loading Login Page...")
    time.sleep(3)

    errorMessage:str = None
    loginPage = LoginPage(driver)
    basicHomePage: BasicHomePage 
    (basicHomePage, errorMessage) = loginPage.Login(password)
    if basicHomePage is None:
        print(f"Unable to navigate to Basic Home Page: {errorMessage}")
        exit(1)
    
    advHomePage: AdvanceHomePage
    (advHomePage, errorMessage) = basicHomePage.NavigateTo_AdvancedPage()
    if advHomePage is None:
        print(f"Unable to navigate to Advanced Page: {errorMessage}")
        exit(1)
    
    sysToolsPanel: SystemToolsPanel
    (sysToolsPanel, errorMessage) = advHomePage.Expand_SystemTools()
    if sysToolsPanel is None:
        print(f"Unable to expand System Tools Panel {errorMessage}")
        exit(1)
    
    fwUpgradeView: FirmwareUpgradeView
    (fwUpgradeView, errorMessage) = sysToolsPanel.NavigateToFirmwareUpgrade()
    if fwUpgradeView is None:
        print(f"Unable to navigate to Firmware Upgrade view. {errorMessage}")
        exit(1)
    
    updateAvailable:bool
    (updateAvailable, errorMessage) = fwUpgradeView.IsUpdateAvailable()
    if updateAvailable is None:
        print(f"Unable to click on 'Check for upgrade' button. {errorMessage}")
        exit(1)
    else:
        print(f"Firmware update available: {str(updateAvailable)}. Status: {errorMessage}")
    driver.quit()
    exit(0)

    #driver.save_screenshot("C:\\temp\\test1.png")
    #txtBxLogin = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "login-cnt", " " ))] | //*[(@id = "form-login")] | //*[contains(concat( " ", @class, " " ), concat( " ", "login-field", " " ))] | //*[contains(concat( " ", @class, " " ), concat( " ", "allow-visible", " " ))] | //*[contains(concat( " ", @class, " " ), concat( " ", "l", " " ))]')
    #while(txtBxLogin is None):
    #    time.sleep(1)
    #txtBxLogin.send_keys("~Norby0317")
    #
    #btnLogin = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "login-cnt", " " ))] | //*[(@id = "form-login")] | //*[contains(concat( " ", @class, " " ), concat( " ", "submit", " " ))] | //*[(@id = "login-btn")] | //*[contains(concat( " ", @class, " " ), concat( " ", "button-text", " " ))]')
    #while(btnLogin is None):
    #    time.sleep(1)
    #btnLogin.click()
    #driver.save_screenshot("C:\\temp\\test2.png")
    #print(driver.current_url)
    #driver.quit()

if __name__ == "__main__":
    main()