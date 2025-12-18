class User:

    def __init__(self, username, email, password):
        self.username = username
        self.set_email(email)
        self.password = password

    def get_email(self):
        return self._email
    
    def set_email(self, email):
        self._email = email
    
user1 = User("vignesh", "yoyovigi@gmail.com", 1234)
print(user1.get_email())

# _email protected 
# __email private 

# consenting adults philosophy
