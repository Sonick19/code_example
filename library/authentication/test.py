# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 20:15:47 2023

@author: Sonya
"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import  time
from authentication.models import CustomUser



 
class TestAuthentication(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get("http://localhost:8000/home/register/")
        elem_1 = driver.find_element(By.NAME, "email")
        elem_2 = driver.find_element(By.NAME, "password")
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
        self.email="test_trial@gmail.com"
        self.passw='12345s'
        elem_1.send_keys(self.email)
        elem_2.send_keys(self.passw)
        submit_button.click()


    def test_with_right_info(self):
        driver = self.driver
        driver.get("http://localhost:8000/home/login/")
        elem_1 = driver.find_element(By.NAME, "email")
        elem_2 = driver.find_element(By.NAME, "password")
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
        elem_1.send_keys(self.email)
        elem_2.send_keys(self.passw)
        time.sleep(5)
        submit_button.click()
        time.sleep(2)
        #self.assertNotIn("Enter a valid email address.", driver.page_source)
        #self.assertNotIn("Incorrect Login or Password", driver.page_source)
        self.assertIn("Hello, User", driver.page_source)

    def test_with_wrong_email_or_password(self):
        driver = self.driver
        driver.get("http://localhost:8000/home/login/")
        elem_1 = driver.find_element(By.NAME, "email")
        elem_2 = driver.find_element(By.NAME, "password")
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
        elem_1.send_keys("121313jsdjasjd2@gamil.com")
        elem_2.send_keys("123sd")
        time.sleep(5)
        submit_button.click()
        time.sleep(2)
        #self.assertNotIn("Hello, User", driver.page_source)
        self.assertNotIn("Enter a valid email address.", driver.page_source)
        self.assertIn("Incorrect Login or Password", driver.page_source)
        
        
    def test_log_out(self):
        driver = self.driver
        driver.get("http://localhost:8000/home/login/")
        elem_1 = driver.find_element(By.NAME, "email")
        elem_2 = driver.find_element(By.NAME, "password")
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
        elem_1.send_keys(self.email)
        elem_2.send_keys(self.passw)
        time.sleep(2)
        submit_button.click()
        time.sleep(5)
        log_button=driver.find_element(By.CLASS_NAME, "button")
        log_button.click()
        time.sleep(2)
        self.assertIn("Login to your account", driver.page_source)    
      
              
    def tearDown(self):
        self.driver.close()
        CustomUser.delete_by_email(self.email)

        

if __name__ == "__main__":
    unittest.main()