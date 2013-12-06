# Let's do this!
# nosetests -v
# http://selenium-python.readthedocs.org/en/latest/getting-started.html
# 3
# http://selenium.googlecode.com/git/docs/api/py/index.html

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

voxy = "http://master.pub.voxy.com/"

class CheckHomePage(unittest.TestCase):

    #setup 
    def setUp(self):
        self.driver = webdriver.Firefox()

    #teardown
    def tearDown(self):
        self.driver.close()

    #check home page title
    def test_homepage_title(self):
        d = self.driver
        d.get(voxy)
        self.assertIn("VOXY", d.title)

    #check 
    def test_homepage_elements(self):
    	d = self.driver
        d.get(voxy)
        elem = d.find_element_by_xpath("//*[@id=\"fixed-login\"]/div/div/div/a")
        self.check_element_exists(path)





    #method for checking element exists
    def check_element_exists(x):
        try:
            webdriver.find_element_by_xpath(x)
        except NoSuchElementException:
            return False
        return True






# __main__
if __name__ == "__main__":
    unittest.main()


