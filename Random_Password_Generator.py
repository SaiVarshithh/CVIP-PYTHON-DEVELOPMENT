import random
import string

def generate_password(length, use_upper, use_lower, use_num, use_spcl_chars):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_num:
        characters += string.digits
    if use_spcl_chars:
        characters += string.punctuation

    if not characters:
        print("Error: Please select at least one character type.")
        return None

    generated_password = ''.join(random.choice(characters) for _ in range(length))
    return generated_password

def main():
    print("Random Password Generator")
    length = int(input("Enter the password length: "))
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_num = input("Include numbers? (y/n): ").lower() == 'y'
    use_spcl_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_lower, use_num, use_spcl_chars)

    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
