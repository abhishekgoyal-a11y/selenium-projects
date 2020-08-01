import unittest


class apptes(unittest.TestCase):
    @unittest.SkipTest
    def testsearch(self):
        print("this is a testsearch")

    @unittest.skip("i am skiipping this test case")
    def testadvacedsearch(self):
        print("this is a advanced testsearch")

    @unittest.skipIf(1 == 2, "est case")
    def testadvaced(self):
        print("this is a advanced")


if __name__ == "__main__":
    unittest.main()
