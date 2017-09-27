users = []
shopping_list = []


from datetime import datetime


class User(object):

    def __init__(self, firstname, lastname, username, email, password):

        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password


class Shoppinglist(object):

    def __init__(self, shoppinglist, description, items, status='new', dateadded='datetime.now()'):
        #self.listid = random.randrange(1, 1000, 1)
        self.shoppinglist = shoppinglist
        self.description = description
        self.items = items
        self.status = 'new'
        self.dateadded = datetime.now().strftime('%Y-%m-%d')

        shopping_list.append(self)

    def delete_list(self, listid):
        shopping_list.remove(self)
