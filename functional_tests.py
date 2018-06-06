from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import unittest


class NewVisitorTest(unittest.TestCase):

        def setUp(self):
            self.browser = webdriver.Firefox()

        def tearDown(self):
            self.browser.quit()

        def test_can_start_a_list_and_retrieve_it_later(self):

            # To see the webpage you need to go to the homepage
            self.browser.get('http://localhost:8000')

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
            self.assertTrue(
                any(row.text == '1: Drink Margarittas' for row in rows),
                "New to-do item not appear in table"
            )

            # You still see the box inviting to add another item, You enter
            # "Drink Cuba Libres"
            self.fail('Finish the test!')

            # Page updates again, showing both items on the lists

            # Sites creates an unique URL for user to remember the list
            #-- it needs some exlanatory text

            # You vistit the page again, the list is still there

            # You are happy, you quit your browser and go mix your drinks

if __name__ == '__main__':
    unittest.main(warnings='ignore')
