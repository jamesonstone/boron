# Let's do this!
# nosetests -v --nocapture
# http://selenium-python.readthedocs.org/en/latest/getting-started.html
# http://selenium.googlecode.com/git/docs/api/py/index.html

import unittest
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException
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

    #check "Start your free 7-day trial today!" button displays
    def test_homepage_elements(self):
    	d = self.driver
        d.get(voxy)
        d.find_element_by_xpath("//*[@id=\"fixed-login\"]/div/div/div/a")
        print "found register button"
        d.find_element_by_xpath("//*[@id=\"header_login_Btn\"]")












# __main__
if __name__ == "__main__":
    unittest.main()




'''
    incorrect xpath
    self.check_element_exists("//*[@id=\"fixed-login\"]/div/div/div/a_")
    self.check_element_exists("//*[@id=\"fixed-login\"]/div/div/div/a")

    def is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except NoSuchElementException, e: return False
    return True

    def check_element_exists(self, x):
    try:
    if self.driver.find_element_by_xpath(x) is None:
    print "Failed Cannot Find"
    except NoSuchElementException:
    return False
'''