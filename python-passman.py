# Importing required libraries
import hashlib  # Library for hashing passwords securely
import getpass  # Library for securely accepting password input without displaying it

# Dictionary to store username and hashed password pairs
password_manager = {}

# Function to create a new user account
def create_account():
    # Prompt user for a desired username
    username = input("Enter your desired username: ")
    
    # Prompt user for a password (input is hidden for security)
    password = getpass.getpass("Enter your desired password: ")
    
    # Hash the password using SHA-256 for secure storage
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    # Store the username and hashed password in the password manager
    password_manager[username] = hashed_password
    
    # Confirm account creation
    print("Account created successfully!")

# Function to log in an existing user
def login():
    # Prompt user for their username
    username = input("Enter your username: ")
    
    # Prompt user for their password (input is hidden for security)
    password = getpass.getpass("Enter your password: ")
    
    # Hash the input password for comparison
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    # Check if the username exists and the hashed password matches the stored one
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        # Login successful
        print("Login successful!")
    else:
        # Login failed due to invalid username or password
        print("Invalid username or password. ")

# Main function to drive the program
def main():
    while True:
        # Display options to the user
        choice = input("Enter 1 to create an account, 2 to login, or 0 to exit: ")
        
        # Handle user choices
        if choice == "1":
            create_account()  # Call function to create an account
        elif choice == "2":
            login()  # Call function to log in
        elif choice == "0":
            break  # Exit the program
        else:
            # Handle invalid input
            print("Invalid choice.")

# Entry point of the program
if __name__ == "__main__":
    main()  # Start the program