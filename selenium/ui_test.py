from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('http://localhost:8000')

body = driver.find_elements(By.XPATH, "//body")
text = body[0].text

blabla: int = 'str'


import unittest

class Test_Rugby(unittest.TestCase):
    
    def setUp(self) -> None:
        self.my_message = 0
    
    def test_inputExists(self):
        self.assertIsNotNone(self.my_message)
        
    def test_inputType(self):
        self.assertIsInstance(self.my_message, int)
        
    def test_length(self):
        self.assertEqual(0, 0)
        
    def test_component_of(self):
        self.assertIn('0 et', '0 et')
        
        
if __name__ == "__main__":
    unittest.main()


driver.close()