from Utilities.yaml_functions import YAML_Reader
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException

class Test_Sauce_YAML:
    def test_sauce_login(self):

        file_name = 'C:\\Users\\Vaithees\\Desktop\\Guvi online class\\KDTF\\TestData\\config.yaml'
        yaml_reader = YAML_Reader(file_name)

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        try:
            
            driver.maximize_window()
            driver.get(yaml_reader.reader()['url'])
            driver.implicitly_wait(10)

           
            driver.find_element(By.ID, yaml_reader.reader()['username_locator']).send_keys(yaml_reader.reader()['username'])
            driver.find_element(By.ID, yaml_reader.reader()['password_locator']).send_keys(yaml_reader.reader()['password'])
            driver.find_element(By.ID, yaml_reader.reader()['login_button_locator']).click()

            
            driver.find_element(By.ID, yaml_reader.reader()['logout_button_locator']).click()
            driver.find_element(By.ID, yaml_reader.reader()['checkout_button']).visible()

           
            screenshot_path = "checkout_overview.png"
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved at {screenshot_path}")

            
            output_path = "C:\\Users\\Vaithees\\Desktop\\Guvi online class\\KDTF\\TestScripts\\checkout_overview.png"
            with open(screenshot_path, "rb") as input_file:
                screenshot_data = input_file.read()

            with open(output_path, "wb") as output_file:
                output_file.write(screenshot_data)
            print(f"Downloadable screenshot saved at {output_path}")

        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR:", error)

        finally:
            driver.quit()
