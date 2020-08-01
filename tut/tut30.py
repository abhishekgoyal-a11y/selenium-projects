import unittest
from selenium import webdriver

# class apptesting(unittest.TestCase):
#     def testsearch(self):
#         print("this is a testsearch")

#     def testadvacedsearch(self):
#         print("this is a advanced testsearch")


class engine(unittest.TestCase):
    def testgoogle(self):
        self.driver = webdriver.Chrome(
            'C:/Users/HP/Desktop/Drivers/chromedriver_win32/chromedriver.exe')
        self.driver.get('https://www.google.com/')
        print(self.driver.title)
        self.driver.close()

    def testyahoo(self):
        self.driver = webdriver.Chrome(
            'C:/Users/HP/Desktop/Drivers/chromedriver_win32/chromedriver.exe')
        self.driver.get('https://in.yahoo.com/')
        print(self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
