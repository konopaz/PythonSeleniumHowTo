import unittest
import test_address_index
import test_address_add

allTests = unittest.TestSuite()
allTests.addTest(test_address_index.suite())
allTests.addTest(test_address_add.suite())
unittest.TextTestRunner().run(allTests)
