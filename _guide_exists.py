import unittest
import wd.parallel
from selenium import webdriver
import copy

class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        desired_capabilities = []

        browser = copy.copy(webdriver.DesiredCapabilities.FIREFOX)
        browser['version'] = '10'
        browser['platform'] = 'XP'
        browser['name'] = 'Python at Sauce 1/2'
        browser['tags'] = "Parallel"
        desired_capabilities += [browser]

        browser = copy.copy(webdriver.DesiredCapabilities.FIREFOX)
        browser['version'] = '10'
        browser['platform'] = 'LINUX'
        browser['name'] = 'Python at Sauce 2/2'
        browser['tags'] = "Parallel"
        desired_capabilities += [browser]

        self.drivers = wd.parallel.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://jameson:f08b27e8-a9ec-4032-a3da-6d46b14551af@ondemand.saucelabs.com:80/wd/hub"
        )


    @wd.parallel.multiply
    def test_sauce(self):
        self.driver.get('http://www.voxy.com')
        # self.assertTrue("I am a page title - Sauce Labs" in self.driver.title);
        print self.driver.title

        # self.driver.find_element_by_id('comments').send_keys('Hello! I am some example comments. I should appear in the page after you submit the form')
        # self.driver.find_element_by_id('submit').click()

        # comments = self.driver.find_element_by_id('your_comments')
        # self.assertTrue('Your comments: Hello! I am some example comments. I should appear in the page after you submit the form' in comments.text)
        # print "Comments are ok"

        # body = self.driver.find_element_by_xpath('//body')
        # self.assertFalse('I am some other page content' in body.text)
        # self.driver.find_elements_by_link_text('i am a link')[0].click()
        # body = self.driver.find_element_by_xpath('//body')
        # self.assertTrue('I am some other page content' in body.text)
        # print "Body is ok"

    @wd.parallel.multiply
    def tearDown(self):
        self.driver.quit()
        print "Quit"

if __name__ == '__main__':
    unittest.main()
