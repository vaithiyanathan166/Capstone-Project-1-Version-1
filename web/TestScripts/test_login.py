
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from TestLocators.locators import SauceLocators
from TestData.data import SauceData
from Utilities.excel_function import ExcelFunctions

class TestSauceDDTF:

    def test_login_excel(self):
        self.excel_file = SauceData().excel_file
        self.sheet_number = SauceData().sheet_number

        self.excel = ExcelFunctions(self.excel_file, self.sheet_number)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
        self.driver.get(SauceData().url)
        self.driver.maximize_window()

        self.driver.implicitly_wait(10)
        self.rows = self.excel.row_count()

       
        for row in range(2, self.rows+1):
            username = self.excel.read_data(row, 5)
            password = self.excel.read_data(row, 6)

            
            self.driver.find_element(by=By.ID, value=SauceLocators.username_locator).send_keys(username)
            self.driver.find_element(by=By.ID, value=SauceLocators.password_locator).send_keys(password)
            self.driver.find_element(by=By.ID, value=SauceLocators.loginbutton_locator).click()

            if SauceData().dashboard_url in self.driver.current_url:
                print("SUCCESS : Login Successful")
                self.excel.write_data(row, 7, "Test Pass")
                self.driver.back()

            elif SauceData().url in self.driver.current_url:
                print("FAIL : Login Failed")
                self.excel.write_data(row, 7, "Test Fail")
                self.driver.refresh()
            
        self.driver.quit()