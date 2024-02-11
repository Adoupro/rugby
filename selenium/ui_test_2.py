from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/')

xpath = "/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]"
element = driver.find_element(By.XPATH, xpath)
element.click()

time.sleep(5)

xpath = "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input"
element = driver.find_element(By.XPATH, xpath)
element.send_keys("Libéré délivré")
element.send_keys(Keys.ENTER)

time.sleep(5)

#element.send_keys("Libéré délivré")
#element.send_keys(Keys.ENTER)
driver.close()


import unittest

class Test_My_App(unittest.TestCase):
    
    
    def setUp(self):
        self.my_message_1 = "Helloo"
        
    def test_testelement(self):
        return self.assertEqual(0, 0, msg="It is ok")
    
    
    
if __name__ == '__main__':
    unittest.main()

