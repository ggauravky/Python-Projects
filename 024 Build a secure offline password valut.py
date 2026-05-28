"""
Challenge: Offline Credential Manager

Create a CLI tool to manage login credentials (website, username, password) in an encoded local file (`vault.txt`).

Your program should:
1. Add new credentials (website, username, password)
2. Automatically rate password strength (weak/medium/strong)
3. Encode the saved content using Base64 for simple offline obfuscation
4. View all saved credentials (decoding them)
5. Update password for any existing website entry (assignment)

Bonus:
- Support searching for a website entry
- Mask password when showing in the list
"""
import base64
import os

VAULT_FILE = 'vault.txt'

def encode(text):
    return base64.b64encode(text.encode()).decode()

def decode(encoded_text):
    return base64.b64decode(encoded_text.encode()).decode()

def password_strength(password):
    if len(password) < 6:
        return 'weak'
    elif len(password) < 12:
        return 'medium'
    else:
        return 'strong'
    
def add_credentials():
    input_website = input("Enter website: ")
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")
    
    strength = password_strength(input_password)
    print(f"Password strength: {strength}")
    credentials = f"{input_website}:{input_username}:{input_password}"
    encoded_credentials = encode(credentials)
    with open(VAULT_FILE, 'a') as f:
        f.write(encoded_credentials + '\n')
        
    print("Credentials added successfully!")

def view_credentials():
    if not os.path.exists(VAULT_FILE):
        print("No credentials found.")
        return
    
    with open(VAULT_FILE, 'r') as f:
        for line in f:
            encoded_credentials = line.strip()
            credentials = decode(encoded_credentials)
            website, username, password = credentials.split(':')
            masked_password = '*' * len(password)
            print(f"Website: {website}, Username: {username}, Password: {masked_password}")
            
def main():
    while True:
        print("\n1. Add Credentials")
        print("2. View Credentials")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_credentials()
        elif choice == '2':
            view_credentials()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")
            
if __name__ == "__main__":
    main()