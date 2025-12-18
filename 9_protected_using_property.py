class Person:

    def __init__(self, user, email):
        self.user = user 
        self._email = email
        
    @property
    def email(self):
        print("Email accessed")
        return self._email
    
    @email.setter
    def email(self, new_email):
        if '@' in new_email:
            print("Email updated")
            self._email = new_email


p1 = Person("vignesh", "yoyovigi@gmail.com")
p1.email = "test@gmail.com"
print(p1.email)