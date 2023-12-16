"""PASSWORD GENERATOR"""
import random
import string

"""generate password"""
def generate_password(length, uppercase, digits, special_chars):
    characters = string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation
    if uppercase:
        characters += string.ascii_uppercase

    if not characters:
        print("Error: Please select at least one character set.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to Password Generator!")

    length = int(input("Enter the length of the password: "))
    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, uppercase, digits, special_chars)

    if password:
        print(f"\nThe generated password is: {password}")

if __name__ == "__main__":
    main()
