from main import Cart
import unittest
class CartTest(unittest.TestCase):

    def test_add(self):
        test_cart = Cart()
        test_cart.add('banana', 1, 0)
        self.assertIn('banana', test_cart.items)
        self.assertEqual(test_cart.items['banana'].quantity, 1)
        self.assertEqual(test_cart.items['banana'].price, 0)
        
    def test_show(self):
        test_cart = Cart()
        test_cart.add('banana', 1, 0)
        self.assertIn('banana', test_cart.items)
        self.assertEqual(test_cart.items['banana'].quantity, 1)
        self.assertEqual(test_cart.items['banana'].price, 0)
        
    def test_delete(self):
        test_cart = Cart()
        test_cart.add('banana', 1, 0)
        self.assertIn('banana', test_cart.items)
        self.assertEqual(test_cart.items['banana'].quantity, 1)
        self.assertEqual(test_cart.items['banana'].price, 0)
        
        test_cart.delete('banana')
        self.assertNotIn('banana', test_cart.items)
unittest.main()