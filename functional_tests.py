from selenium import webdriver
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
            self.fail('Finish the test!')

            # You can enter your todo right away

            # You type "Drink Margarittas" as you are filthy alcoholic

            # When you hit enter, the page updates, and lists:
            # "1: Drink Margarittas" as an item in a to-do lists

            # You still see the box inviting to add another item, You enter
            # "Drink Cuba Libres"

            # Page updates again, showing both items on the lists

            # Sites creates an unique URL for user to remember the list
            #-- it needs some exlanatory text

            # You vistit the page again, the list is still there

            # You are happy, you quit your browser and go mix your drinks

if __name__ == '__main__':
    unittest.main(warnings='ignore')
