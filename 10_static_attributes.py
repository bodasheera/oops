class User:

    user_count = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email

        User.user_count += 1

u1 = User("a", "a")
u2 = User("b", "b")
print(User.user_count)