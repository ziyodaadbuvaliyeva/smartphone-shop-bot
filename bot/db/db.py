import json


class UserDB:
    def __init__(self, db_file='data/users.json'):
        self.db_file = db_file
        self.load()

    def load(self):
        try:
            with open(self.db_file, 'r') as f:
                self.users = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.users = {}

    def save(self):
        with open(self.db_file, 'w') as f:
            json.dump(self.users, f, indent=4)

    def get_user(self, user_id):
        return self.users.get(str(user_id), {})

    def set_user(self, user_id, data):
        self.users[str(user_id)] = data
        self.save()

class SmartPhoneDB:
    def __init__(self, db_file='data/smartphones.json'):
        self.db_file = db_file
        self.load()

    def load(self):
        try:
            with open(self.db_file, 'r') as f:
                self.phones = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.phones = {}

    def get_iphone_x(self):
        return self.phones['apple']['iPhoneX']
