class User:
    def __init__(self,username, name, email):
        self.username = username
        self.name = name
        self.email = email
        print("User Created!")

    def introduce_yourself(self, guest_name):
        print("Hi {}, I'm{}! contact me at {}.".format(guest_name, self.name, self.email))

    def __repr__(self):
        return "User(username={}, name={}, email={}).".format(self.username, self.name, self.email)
        
    def __str__(self):
        return self.__repr__()


akash = User("akash","Akash Kumar","akash@example.com")
shubham = User("shubham","Shubham Kumar","shubham@example.com")
nitin = User("nitin","Nitin Kumar","nitin@example.com")
nitish = User("nitish","Nitish Kumar","nitish@example.com")
gaurav = User("gaurav","Gaurav Kumar","gaurav@example.com")
snehil = User("snehil","Snehil Kumar","snehil@example.com")

users = [akash, shubham, nitin, nitish, gaurav, snehil]

class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0 # setting the initial counter 0
        while i < len(self.users): # looping through all the valid cases
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user) # inserts the user on the required index

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
    
    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return print(self.users)
    
database = UserDatabase()

database.insert(akash)
database.insert(shubham)
database.insert(snehil)

user = database.find("snehil")
print(user)

database.update(User(username="snehil", name="Snehil Shankar", email="shankar.snehil@gmail.com"))

print(user)

database.insert(nitin)

database.list_all()