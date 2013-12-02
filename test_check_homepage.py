# Let's do this!
# nosetests -v
# http://selenium-python.readthedocs.org/en/latest/getting-started.html
# http://www.seleniumhq.org/docs/03_webdriver.jsp#chapter03-reference
# http://selenium.googlecode.com/git/docs/api/py/index.html

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

voxy = "http://www.voxy.com/"

class CheckHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_homepage_title(self):
        driver = self.driver
        driver.get(voxy)
        self.assertIn("VOXY", driver.title)

    def test_homepage_elements(self):
    	driver = self.driver
    	driver.get(voxy)
    	# driver.find_elements_by_xpath("//*[@id=\"fixed-login\"]/div/div/div/a__")
    	#driver.implicitly_wait(8)
    	try:	
    		if driver.find_elements_by_xpath("//*[@id=\"fixed-login\"]/div/div/div/a"):
             return True
    		#driver.find_element(By.LINK_TEXT, "Start your free 7-day trial today!")
    	except:
    		return False

    def tearDown(self):
        self.driver.close()











# __main__
if __name__ == "__main__":
    unittest.main()