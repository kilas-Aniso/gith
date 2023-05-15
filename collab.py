users = {"user1": "password1", "user2": "password2", "user3": "password3"}

# Get user input
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if username and password are correct
if username in users and users[username] == password:
    print("Login successful!")
else:
    print("Invalid username or password.")