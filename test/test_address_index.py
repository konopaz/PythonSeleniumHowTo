import selenium.webdriver
import unittest

def suite():
  suite = unittest.TestLoader().loadTestsFromTestCase(AddressesIndexTestCase)
  return suite

class AddressesIndexTestCase(unittest.TestCase):

  def setUp(self):
    self.driver = selenium.webdriver.Firefox()
    self.driver.get("http://localhost:8080/addressbook")
    self.assertEqual("http://localhost:8080/addressbook", self.driver.current_url)
    self.assertEqual("Addresses", self.driver.title)

  def tearDown(self):
    self.driver.close()

  def test_index_loads(self):
    addressDivs = self.driver.find_elements_by_css_selector("div.addresses > div")
    self.assertIsNotNone(addressDivs)
    self.assertTrue(0 < len(addressDivs))

  def test_index_add_link(self):
    self.driver.find_element_by_id("add-address").click()
    self.assertEqual("http://localhost:8080/addressbook/add", self.driver.current_url)
    self.assertEqual("Add Address", self.driver.title)

if __name__ == "__main__":
  unittest.main()
