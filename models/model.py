users=[]
shopping_list=[]
class User(object):
    
    def __init__(self,firstname,lastname,username,email,password):
        
        self.first_name=firstname
        self.last_name=lastname
        self.username=username
        self.email=email
        self.password=password

class Shoppinglist(object):
    def __init__(self,shoppinglist,description,items,status,dateadded):
        
        self.shoppinglist=shoppinglist
        self.description=description
        self.items=items
        self.status=status
        self.dateadded=dateadded
        