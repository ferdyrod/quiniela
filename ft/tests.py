from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.test import LiveServerTestCase
from django.core.management import call_command

class AdminTest(LiveServerTestCase):

    # Load Fixture
    # fixtures = ['/ft/fixtures/admin.json',]

    def setUp(self):
        self.browser = webdriver.Firefox()
        call_command('loaddata', 'ft/fixtures/admin.json', verbosity=0)

    def tearDown(self):
        self.browser.quit() 

    def test_admin_site(self):
        # User opens web browser and navigates to the admin page'''
        self.browser.get(self.live_server_url + '/admin/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)
        # User types in username and password and presses enter
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('admin')
        password_field.send_keys(Keys.RETURN)
        # Login credentiasl are corret and the user is redirected to the main admin page
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)
        # user clicks on the Users link
        user_link = self.browser.find_elements_by_link_text('Users')
        user_link[0].click()
        # User verifies that user frodriguez@gmail.com is present
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('frodriguez@gmail.com', body.text)
