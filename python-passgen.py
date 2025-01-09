# Password Generator
# This code generates a secure, random password with a specified length (default 10 characters). 
# It ensures that the password contains at least one uppercase letter, one lowercase letter, one digit, and one punctuation character, 
# fulfilling common complexity requirements. After ensuring these criteria are met, it randomly selects additional characters from the 
# available character sets to complete the desired password length. Finally, it shuffles the characters to avoid predictable patterns 
# and returns the password as a string.
import random
import string

def generate_password(length: int = 10):
    if length < 4:
        raise ValueError("Password length must be at least 4 to satisfy complexity requirements.")
    
    # Define the required character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    punctuation = string.punctuation
    
    # Ensure the password has at least one character from each set
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(punctuation)
    ]
    
    # Fill the rest of the password length with random characters from all sets
    alphabet = uppercase + lowercase + digits + punctuation
    password += [random.choice(alphabet) for _ in range(length - 4)]
    
    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)
    
    # Join the list into a string and return it
    return ''.join(password)

password = generate_password()
print(f"Generated password: {password}")

if __name__ == "__main__":
    generate_password
