
class User:
    active_user = 0

    @classmethod
    def display_active_user(cls):
        return f"There are currently {cls.active_user} active users"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, age)


    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = max(age, 0)
        User.active_user += 1

    def logout(self):
        User.active_user -= 1

    def initials(self):
        return f"{self.first[0]}{self.last[0]}"

class Moderator(User):

    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
    def remove_post(self):
        print(f"remove post for {self.first} from community {self.community}")


user1 = User("wendu", "hu", 27)
user2 = User("seg", "ki", 26)
print(User.active_user)
user3 = Moderator("xs", "oi", 25, "Sports")
print(User.active_user)
print(user3.initials())
print(user3.remove_post())
user2.logout()
print(user3.display_active_user())
print(User.display_active_user())     ## class methods相当于static method


