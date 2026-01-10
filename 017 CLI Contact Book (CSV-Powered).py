"""
 Challenge: CLI Contact Book (CSV-Powered)

Create a terminal-based contact book tool that stores and manages contacts using a CSV file.

Your program should:
1. Ask the user to choose one of the following options:
   - Add a new contact
   - View all contacts
   - Search for a contact by name
   - Exit
2. Store contacts in a file called `contacts.csv` with columns:
   - Name
   - Phone
   - Email
3. If the file doesn't exist, create it automatically.
4. Keep the interface clean and clear.

Example:
Add Contact
View All Contacts
Search Contact
Exit

Bonus:
- Format the contact list in a table-like view
- Allow partial match search
- Prevent duplicate names from being added
"""

import csv
import os

FILENAME = "contacts.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email"])


def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone: ").strip()
    email = input("Enter Email: ").strip()

    with open(FILENAME, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Name"].lower() == name.lower():
                print("Contact with this name already exists.")
                return

    with open(FILENAME, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])
        print("Contact added successfully.")


def view_contacts():
    with open(FILENAME, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        contacts = list(reader)
        if not contacts:
            print("No contacts found.")
            return

        print(f"{'Name':<20} {'Phone':<15} {'Email':<30}")
        print("-" * 65)
        for row in contacts:
            print(f"{row['Name']:<20} {row['Phone']:<15} {row['Email']:<30}")


def search_contact():
    search_name = input("Enter name to search: ").strip().lower()
    found = False

    with open(FILENAME, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print(f"{'Name':<20} {'Phone':<15} {'Email':<30}")
        print("-" * 65)
        for row in reader:
            if search_name in row["Name"].lower():
                print(f"{row['Name']:<20} {row['Phone']:<15} {row['Email']:<30}")
                found = True

    if not found:
        print("No matching contacts found.")

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Search for a contact by name")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Exiting the contact book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()