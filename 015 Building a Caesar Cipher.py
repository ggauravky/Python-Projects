"""
Building a Caesar Cipher

Challenge: Secret Message Encryptor & Decryptor

Create a Python script that helps you send secret messages to your friend using simple encryption.

Your program should:
1. Ask the user if they want to (E)ncrypt or (D)ecrypt a message.
2. If encrypting:
   - Ask for a message and a numeric secret key.
   - Use a Caesar Cipher (shift letters by the key value).
   - Output the encrypted message.
3. If decrypting:
   - Ask for the encrypted message and key.
   - Reverse the encryption to get the original message.

Rules:
- Only encrypt letters; leave spaces and punctuation as-is.
- Make sure the letters wrap around (e.g., 'z' + 1 → 'a').

Bonus:
- Allow uppercase and lowercase letter handling
- Show a clean interface
"""


def caesar_cipher(message, key):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shifted = (ord(char) - base + key) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result


def decrypt_caesar_cipher(message, key):
    return caesar_cipher(message, -key)


def get_action():
    while True:
        action = (
            input("Would you like to (E)ncrypt or (D)ecrypt a message? ")
            .strip()
            .lower()
        )
        if action in ("e", "encrypt"):
            return "encrypt"
        if action in ("d", "decrypt"):
            return "decrypt"
        print("Invalid option. Please choose either (E)ncrypt or (D)ecrypt.")


def get_key():
    while True:
        key_input = input("Enter the numeric secret key (shift value): ").strip()
        try:
            return int(key_input)
        except ValueError:
            print("Please enter a valid numeric key (e.g., 3).")


def main():
    print("Welcome to the Caesar Cipher Encryptor & Decryptor!")
    action = get_action()

    if action == "encrypt":
        text = input("Enter the message to encrypt: ")
        key = get_key()
        encrypted_message = caesar_cipher(text, key)
        print(f"Encrypted Message: {encrypted_message}")
    else:
        text = input("Enter the message to decrypt: ")
        key = get_key()
        decrypted_message = decrypt_caesar_cipher(text, key)
        print(f"Decrypted Message: {decrypted_message}")


if __name__ == "__main__":
    main()
