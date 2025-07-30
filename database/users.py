import json


def load_users():
    """Load users from the JSON file."""
    try:
        with open('data/users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
def save_users(users):
    """Save users to the JSON file."""
    with open('data/users.json', 'w') as file:
        json.dump(users, file, indent=4)

def get_user(user_id):
    """Get a user by user_id."""
    users = load_users()
    return users.get(str(user_id), None)

def add_user(user_id, user_data):
    """Add a new user to the database."""
    if get_user(user_id):
        return
    users = load_users()
    users[user_id] = user_data
    save_users(users)

def update_user(user_id, user_data):
    """Update an existing user."""
    users = load_users()
    if user_id in users:
        users[user_id].update(user_data)
        save_users(users)
    else:
        raise ValueError("User not found")
    