from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):



    def wait_for_row_in_list_table(self, row_text):
        
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
                    
                

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
        

    def test_can_start_a_list_for_one_user(self):

        # To see the webpage you need to go to the homepage
        self.browser.get(self.live_server_url)


        # You can easly know you are in correct place by the title and header
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)


        # You can enter your todo right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
            )

        # You type "Drink Margarittas" as you are filthy alcoholic
        inputbox.send_keys('Drink Margarittas')

        # When you hit enter, the page updates, and lists:
        # "1: Drink Margarittas" as an item in a to-do lists
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Drink Margarittas')

        # You still see the box inviting to add another item, You enter
        # "Drink Cuba Libres"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Drink Cuba Libres')
        inputbox.send_keys(Keys.ENTER)



        # Page updates again, showing both items on the lists

        self.wait_for_row_in_list_table('2: Drink Cuba Libres')
        self.wait_for_row_in_list_table('1: Drink Margarittas')
        # You are happy, you quit your browser and go mix your drinks
        
    def test_multiple_users_can_start_lists_at_diffrent_urls(self):
        
        #Edith starts a new to-do list.
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Drink Margarittas')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Drink Margarittas')
        
        #She notices that her list has a unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        #Now a new user, Francis, comes along to the site.

        ##We use a new browser session to make sure that no information
        ##of Edith's is coming through from cookies etc

        self.browser.quit()
        self.browser = webdriver.Firefox()

        #Francis visits the home page. There is no sign of Edith's list

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Drink Margarittas', page_text)
        self.assertNotIn('Cuba Libres', page_text)

        #Francis is starting a new list by entering a new item.

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        #Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        #Again there is no trace of Edith's list

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Drink Margarittas', page_text)
        self.assertNotIn('Cuba Libres', page_text)



        #Satisfied, they both go back to sleep (together ?)

#        self.fail('Finish the test!')

