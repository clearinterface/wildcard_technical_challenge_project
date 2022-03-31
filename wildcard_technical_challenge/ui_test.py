import os
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class FormSubmission(unittest.TestCase):
    def setUp(self):
        # creating temporary directory
        try:
            os.mkdir('tmp')
        except FileExistsError:
            pass

        # creating directory to Append Driver
        try:
            os.mkdir('tmp/driver')
        except FileExistsError:
            pass

        # initialize the browser
        self.driver = webdriver.Chrome(ChromeDriverManager(path='tmp/driver').install())

    def tearDown(self):
        self.driver.quit()


    # the unittest
    def test_start_web(self):
        url: str = 'http://localhost:8080/'
        self.driver.get(url=url)

        self.assertEqual('client', self.driver.title)

    def test_send_web(self):
        url: str = 'http://localhost:8080/'
        self.driver.get(url=url)
        filtered_words_element = self.driver.find_element(By.NAME,"filtered_words")
        filtered_words_element.send_keys("into lowest,through \"anger and disgust\" \"But that point was decided\"")
        document_text_element = self.driver.find_element(By.NAME, "document_text")
        document_text_element.send_keys("It went through such rapid contortions that the little bear was forced to change his hold on it so many times he became confused in the darkness, and could not, for the life of him, tell whether he held the sheep right side up, or upside down. But that point was decided for him a moment later by the animal itself, who, with a sudden twist, jabbed its horns so hard into his lowest ribs that he gave a grunt of anger and disgust.")
        form_element = self.driver.find_element(By.NAME, "form-words")
        form_element.submit()
        error_value = self.driver.find_element(By.XPATH, "//div//p[@id='error']")
        self.assertNotEqual('Error: Network Error', error_value.text, "API is running")

if __name__ == '__main__':
    unittest.main()