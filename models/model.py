users = []
shopping_list = []

from datetime import datetime
 
class User(object):

    def __init__(self, firstname, lastname, username, email, password):

        self.id = id(self)
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password


class Shoppinglist(object):

    def __init__(self, shoppinglist, description, items, status='new', dateadded='datetime.now()'):
        self.listid = id(self)
        self.shoppinglist = shoppinglist
        self.description = description
        self.items = items
        self.status = 'new'
        self.dateadded = datetime.now().strftime('%Y-%m-%d')

