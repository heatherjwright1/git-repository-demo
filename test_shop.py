#Write unit tests for your Simple Shop Program in Task 3.
##You may need to refactor your function in Task 3 to ‘untangle’ some logic into smaller blocks of code to make it easier to write tests.
#Write at least 5 unit tests in total covering various and appropriate cases. 
#An expected test will see your custom error being raised.

import unittest
from shop.py import

class ShopProgramTestCase(unittest.Testcase):
        
# Test 1
def test_add_money_invalid(self):
    available_money = 100
    amount = 0
    expected_balance = 100
    new_balance = add_money(available_money, amount)
    self.asertEqual(new_balance, expected_balance)

# Test 2
    def test_add_money_to_balance(self):
            available_money = 100
            amount = 60
            expected_balance = 160
            new_balance = add_money(available_money, amount)
            self.assertTrue(new_balance, expected_balance)

# Test 3
    def test_user_unable_to_purchase(self):
            key = 'jacket'
            price = 160
            available_money = 100
            testValue = False
            result = purchase_item(key, price, available_money)
            self.assertFalse(testValue, result)

# Test 4
def test_maximum_number_of_attempts(self):
 purchase_attempts = 2
expected_purchase_attempts = 3
user_input = 'yes'
result = ask_to_add_money(purchase_attempts, user_input)
self.assertEqual(result, expected_purchase_attempts)

# Test 5
def user_able_to_purchase(self):
     key = 'shoes'
     price = 149
     available_money = 200
     result = purchase_item(key, price, available_money)
     self.assertTrue(result)