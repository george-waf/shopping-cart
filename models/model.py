class User(object):
    users = []

    def register(self,firstname,lastname,email,username,password):
        self.users.append([firstname,lastname,email,username,password])
   
    def userlist(self):
        for i in self.users:
            print (i)
            
    def login(self, email, password):
        pass

class ShoppingCart(object):

    def __init__(self):
        self.shoppinglist = []

    def newshoppinglist(self, listname, quantity,idf):
        self.shoppinglist.append([listname,quantity,idf])

    def deletellist(self, listname, quantity,idf):
        self.shoppinglist.remove([listname, quantity,idf])
         
class ShoppingListItem(ShoppingCart):

    def __init__(self):
        self.listname = listname

    def description(self):
        pass
