import random
import string as st
import json

filename = "users.json"
with open(filename, "r") as f:
    data = json.load(f)


class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.tag = str(random.randrange(0, 10000)).zfill(4)
        self.id = UserDatabase.create_id()
        self.token = UserDatabase.create_token()

    def __repr__(self):
        return f"<User id='{self.id}'" \
               f" name='{self.name}'" \
               f" age={self.age}" \
               f" tag='{self.tag}'>"

    @property
    def under_age(self):
        return self.age <= 18

    @property
    def full_name(self):
        return f"{self.name}#{self.tag}"


class UserDatabase:

    @classmethod
    def add_user(cls, new_user: User):
        if not isinstance(new_user, User):
            raise TypeError(f"'{new_user}' has to be an instance of User Class")
        else:
            dictionary = {"name": new_user.name,
                          "age": new_user.age,
                          "tag": new_user.tag,
                          "id": new_user.id,
                          "token": new_user.token,
                          "under_age": new_user.under_age}

            data.append(dictionary)
            with open(filename, "w") as file:
                json.dump(data, file, indent=4, separators=(",", ": "))

            print("User was added successfully")

    @classmethod
    def remove_user(cls, user_id: int):
        for index, dict_ in enumerate(data):
            if dict_["id"] == user_id:
                del data[index]
                with open(filename, "w") as file:
                    json.dump(data, file, indent=4, separators=(",", ": "))
                break
        else:
            raise Exception('Id not found')

    @classmethod
    def print_dict(cls):
        for i in data:
            print(i)

    @classmethod
    def create_id(cls):
        return random.getrandbits(60)

    @classmethod
    def create_token(cls):
        characters = random.choices(st.ascii_letters + st.digits, k=63)

        symbols = [".", ".", random.choice(["-", "_"])]
        start = random.choice(["Nz0", "NzO", "", "CV"])

        for symbol in symbols:
            characters[random.randrange(len(characters))] = symbol

        return f"{start}{''.join(characters)}"

    @classmethod
    def display_users(cls):
        for user in data:
            for key, value in user.items():
                print(f"{key.title()}: {value}")
            print("\n\n")

