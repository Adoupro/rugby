import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('http://localhost:8000/')


def count_ods_row():
    time.sleep(2)
    cout_ods_row_xpath = "/html/body/div"
    element = driver.find_element(By.XPATH, cout_ods_row_xpath)
    element = element.text
    return int(element.split(' : ')[-1])


class ODS_Count(unittest.TestCase):
    
    def setUp(self) -> None:
        self.cout_ods_row = count_ods_row()
        
    def test_type_row(self):
        self.assertIsInstance(count_ods_row(), int)
        
    def test_not_zero(self):
        self.assertGreater(count_ods_row(), 0)
        
    def test_correct_number(self):
        self.assertEqual(count_ods_row(), 20000)
        

if __name__ == "__main__":
    unittest.main()
    driver.close()


driver.close()