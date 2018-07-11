from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
        
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
        

    def test_can_start_a_list_and_retrieve_it_later(self):

        # To see the webpage you need to go to the homepage
        self.browser.get('http://localhost:8000')
        a


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
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Drink Margarittas', [row.text for row in rows])

        # You still see the box inviting to add another item, You enter
        # "Drink Cuba Libres"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Drink Cuba Libres')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)



        # Page updates again, showing both items on the lists

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Drink Margarittas', [row.text for row in rows])
        self.assertIn('2: Drink Cuba Libres', [row.text for row in rows])

        # Sites creates an unique URL for user to remember the list
        #-- it needs some exlanatory text
        self.fail('Finish the test!')
        # You vistit the page again, the list is still there

        # You are happy, you quit your browser and go mix your drinks

if __name__ == '__main__':
    unittest.main(warnings='ignore')
