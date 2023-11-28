import random
import string

def generate_password(length, uppercase, digits, special_chars):
    """Generate a random password based on user preferences."""
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not characters:
        print("Error: Please select at least one character set.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    # Get user preferences
    length = int(input("Enter the length of the password: "))
    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate and display the password
    password = generate_password(length, uppercase, digits, special_chars)

    if password:
        print(f"\nYour generated password is: {password}")

if __name__ == "__main__":
    main()
