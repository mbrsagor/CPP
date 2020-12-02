import json

file_path = 'numbers2.json'

try:
    with open(file_path) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name?: ")
    with open(file_path, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")
