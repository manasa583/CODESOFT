
class Contact:
    def _init_(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class CM:
    def _init_(self):
        self.contacts = []

    def add(self, contact):
        self.contacts.append(contact)

    def view(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone_number}")

    def search(self, query):
        found_contacts = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts

    def update(self, name, new_contact):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone_number = new_contact.phone_number
                contact.email = new_contact.email
                contact.address = new_contact.address

    def delete(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]

def main():
    contact_manager = CM()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_manager.add(contact)
            print("Contact added successfully.")

        elif choice == "2":
            contact_manager.view()

        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            found_contacts = contact_manager.search(query)
            if found_contacts:
                print("Found contacts:")
                for contact in found_contacts:
                    print(f"Name: {contact.name}, Phone: {contact.phone_number}")
            else:
                print("No contacts found.")

        elif choice == "4":
            name = input("Enter name of contact to update: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            new_contact = Contact(name, new_phone_number, new_email, new_address)
            contact_manager.update(name, new_contact)
            print("Contact updated successfully.")

        elif choice == "5":
            name = input("Enter name of contact to delete: ")
            contact_manager.delete(name)
            print("Contact deleted successfully.")

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "_main_":
    main()