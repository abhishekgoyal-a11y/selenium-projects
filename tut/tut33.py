import unittest
from selenium import webdriver


class sdf(unittest.TestCase):
    def testgoogle(self):
        self.driver = webdriver.Chrome(
            'C:/Users/HP/Desktop/Drivers/chromedriver_win32/chromedriver.exe')
        self.driver.get('https://www.google.com/')
        self.name = self.driver.title
        print(self.name)
        self.assertNotEqual("Googl1223e", self.name, "dfhsgsd")


if __name__ == "__main__":
    unittest.main()
