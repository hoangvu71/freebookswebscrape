from selenium import webdriver
import unittest
import time
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_visitor(self):

        self.browser.get('http://localhost:8000')



        ## Edith has heard about a cool new website that she can get ebooks for free!
        ## She checks out the home page
        time.sleep(1)
        self.assertIn('Django', self.browser.title,
                        f'Current title is {self.browser.title}')

        self.fail('Finish the remaining test')

        # From the top down
        # She immediately sees the navigation 
        # It includes home, account

        # Going down, she immediately sees a sort and filter buttons to filter the ebooks

        # Then the main content, the top 20 ebooks from accross many different sites like
        # amazon, barnsandnoble, etc...

        # She is excited but the homepage ebooks have a widerange of genres and she wants
        # to read only Mystery Ebooks

        # She notice the left side widget has genre selection that she can choose from
        # She happily choose her Mystery Selection and then freeebooks for that day show up
        # She is happy and browsing

        # She founded 4 ebooks that she wants to read and she wants to save it somewhere to remember
        # She then clicked on the navigation bar > account

        # This allows her to create an account
        # Once she created her account, she was able to log in and sees her account information

        # She then go back to the Mystery books section and proceed to save ebooks to her account

if __name__ == "__main__":
    unittest.main()