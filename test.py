# from django.db import models

class User():
    def __init__(self, uid, email):
        self.user_id = uid
        self.email = email
    
class UserPin(User):
    def __init__(self, uid):
        User.__init__(self, uid)
        self.pin = '000000'

parent_instance = User()
child_instance = UserPin()
print(child_instance.user_id)