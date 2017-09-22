import unittest
from model import User,Shoppinglist,Shoppinglistitems

class User(unittest.TestCase):
  def setUp(self):
    self.user = User()
    
  def tearDown(self):
    del self.user

  def test_adding_user(self):
      self.user.firstname='george'

class Shoppinglist(unittest.TestCase):
    def setUp(self):
        self.shoppingList = Shoppinglist()

    def test_if_shoppinglist_stauts_is_new(self):
        self.shoppingList.status='new'
    
    def tearDown(self):
        del self.shoppingList
     

class Shoppinglistitems(unittest.TestCase):
  def test_if_shoppinglist_stauts_is_new(self):
       self.status='new'

if __name__ == '__main__':
    unittest.main(verbosity=2)      
