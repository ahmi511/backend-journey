from typing import Dict, Any

# This is a Python Dictionary. Notice how it uses {} and key: value pairs.
# It looks exactly like JSON!
user: Dict[str, Any] = {
    "id": 101,
    "username": "ahmi511",
    "is_active": True,
    "skills": ["C++", "Python", "Linux"]
}

# Let's extract specific data using the keys
print(f"User ID: {user['id']}")
print(f"Username: {user['username']}")

# Let's add a new key-value pair dynamically
user["role"] = "Junior Backend Developer"

print(f"Updated User Profile: {user}")