import selenium.webdriver
import unittest
import random
import time

def suite():
  suite = unittest.TestLoader().loadTestsFromTestCase(AddressesAddTestCase)
  return suite

class AddressesAddTestCase(unittest.TestCase):

  def setUp(self):
    self.driver = selenium.webdriver.Firefox()
    self.driver.get("http://localhost:8080/addressbook/add")
    self.assertEqual("http://localhost:8080/addressbook/add", self.driver.current_url)
    self.assertEqual("Add Address", self.driver.title)

  def tearDown(self):
    self.driver.close()

  def test_address_add(self):
    streetAddress = "285 Edgewater Ln"
    streetAddress = streetAddress + "_" + str(random.randint(1, 99999))
    streetAddress = streetAddress + "_" + str(time.time())
    self.driver.find_element_by_id("address-street").send_keys(streetAddress)
    self.driver.find_element_by_id("address-submit").click()
    self.assertEqual("http://localhost:8080/addressbook", self.driver.current_url)

    addressDivs = self.driver.find_elements_by_css_selector("div.addresses > div")
    self.assertIsNotNone(addressDivs)
    foundAddress = False
    for addressDiv in addressDivs:
      if (streetAddress == addressDiv.text):
        foundAddress = True
    self.assertTrue(foundAddress)

if __name__ == "__main__":
  unittest.main()
