import unittest


def setUpModule():
    print("xgdsg")


def tearDownModule():
    print("sg")


class apptesting(unittest.TestCase):
    # @classmethod
    # def setUp(self):
    #     print("this is login test")

    # @classmethod
    # def tearDown(self):
    #     print("this is logout test")
    @classmethod
    def setUpClass(self):
        print("open application")

    @classmethod
    def tearDownClass(cls):
        print("close application")

    def testsearch(self):
        print("this is a testsearch")

    def testadvacedsearch(self):
        print("this is a advanced testsearch")

    def testadvaced(self):
        print("this is a advanced")


if __name__ == "__main__":
    unittest.main()
