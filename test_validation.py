from seleniumbase import BaseCase
import time

url = "http://air-20.dev.ascensor.co.uk/"

class TestValidation(BaseCase):

    def test_html(self):
        self.open("https://validator.w3.org/")
        self.type("#uri", url)
        self.click("form[method='get'] a[class='submit']")
        self.wait_for_text_visible("Showing results for", timeout=20)

    def test_css(self):
        self.open("https://jigsaw.w3.org/css-validator/")
        self.type("#uri", url)
        self.click("label[title='Submit URI for validation'] span")
        self.wait_for_text_visible("W3C CSS Validator results for", timeout=20)