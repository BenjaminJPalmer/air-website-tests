from seleniumbase import BaseCase
import time

url = "http://air-20.dev.ascensor.co.uk/"

class TestPageSpeed(BaseCase):

    def test_mobile_speed(self):
        self.open("https://developers.google.com/speed/pagespeed/insights/")
        self.type("input[placeholder='Enter a web page URL']", url)
        self.click("div[role='button']")
        self.wait_for_element_visible(".tab-title.tab-desktop", timeout=20)


    def test_desktop_speed(self):    
        self.open("https://developers.google.com/speed/pagespeed/insights/")
        self.type("input[placeholder='Enter a web page URL']", url)
        self.click("div[role='button']")
        self.wait_for_element_visible(".tab-title.tab-desktop", timeout=20)
        self.click(".tab-title.tab-desktop")
    
    def test_my_site(self):
        self.open("https://www.thinkwithgoogle.com/intl/en-gb/feature/testmysite/")
        self.type("#url", url)
        self.click(".arrow.mat-icon.material-icons.active")
        self.wait_for_text_visible("Your mobile page speed is", timeout=30)