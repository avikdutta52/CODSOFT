import random
import string

def generate_password(length):
    # Define character sets for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    # Prompt the user for the desired password length
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length should be a positive number.")
            return
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print(f"Generated password: {password}")
    
    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
